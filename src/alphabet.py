import torch, torch.nn as nn, numpy as np
import json, torch

from src.nltk_utils import bag_of_words, tokenize, stem
from torch.utils.data import Dataset, DataLoader

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        # no activation and no softmax at the end
        return out

class Classify:
    def __init__(self, JSON, FILE):
        self.JSON = JSON
        self.FILE = FILE

        self.tags = None
        self.model = None
        self.device = None
        self.intents = None
        self.all_words = None

    def initalize(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        with open(self.JSON, 'r') as json_data:
            self.intents = json.load(json_data)

        data = torch.load(self.FILE)

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        self.all_words = data['all_words']
        self.tags = data['tags']
        model_state = data["model_state"]

        self.model = NeuralNet(input_size, hidden_size, output_size).to(self.device)
        self.model.load_state_dict(model_state)
        self.model.eval()

    def get_response(self, input_sent):
        sentence = tokenize(input_sent)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(self.device)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        confidence = prob.item()
        if confidence > 0.8:
            for intent in self.intents['intents']:
                response = intent['responses']
                if tag == intent["tag"]: return tag, response

        else: return "default", ""

class Train:
    def __init__(self, intents, outpath):
        self.intents = []
        self.outpath = outpath

        self.num_epochs = 4000
        self.batch_size = 521
        self.learning_rate = 0.001
        self.hidden_size = 521

        with open(intents, 'r') as f:
            self.intents = json.load(f)

    def initalize(self):
        all_words = []
        tags = []
        xy = []

        # loop through each sentence in our self.intents patterns
        for intent in self.intents['intents']:
            tag = intent['tag']
            # add to tag list
            tags.append(tag)
            for pattern in intent['patterns']:
                # tokenize each word in the sentence
                w = tokenize(pattern)
                # add to our words list
                all_words.extend(w)
                # add to xy pair
                xy.append((w, tag))

        # stem and lower each word
        ignore_words = ['?', '.', '!']
        all_words = [stem(w) for w in all_words if w not in ignore_words]

        # remove duplicates and sort
        all_words = sorted(set(all_words))
        tags = sorted(set(tags))

        print(len(xy), "patterns")
        print(len(tags), "tags:", tags)
        print(len(all_words), "unique lemmatized words:", all_words)

        # create training data
        X_train = []
        y_train = []
        for (pattern_sentence, tag) in xy:
            # X: bag of words for each pattern_sentence
            bag = bag_of_words(pattern_sentence, all_words)
            X_train.append(bag)
            # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
            label = tags.index(tag)
            y_train.append(label)

        X_train = np.array(X_train)
        y_train = np.array(y_train)

        # Hyper-parameters
        num_epochs = self.num_epochs
        batch_size = self.batch_size
        learning_rate = self.learning_rate
        hidden_size = self.hidden_size
        input_size = len(X_train[0])
        output_size = len(tags)
        print(input_size, output_size)

        class ChatDataset(Dataset):

            def __init__(self):
                self.n_samples = len(X_train)
                self.x_data = X_train
                self.y_data = y_train

            # support indexing such that dataset[i] can be used to get i-th sample
            def __getitem__(self, index):
                return self.x_data[index], self.y_data[index]

            # we can call len(dataset) to return the size
            def __len__(self):
                return self.n_samples

        dataset = ChatDataset()
        train_loader = DataLoader(dataset=dataset,
                                batch_size=batch_size,
                                shuffle=True,
                                num_workers=0)

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        model = NeuralNet(input_size, hidden_size, output_size).to(device)

        # Loss and optimizer
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        # Train the model
        for epoch in range(num_epochs):
            for (words, labels) in train_loader:
                words = words.to(device)
                labels = labels.to(dtype=torch.long).to(device)

                # Forward pass
                outputs = model(words)
                # if y would be one-hot, we must apply
                # labels = torch.max(labels, 1)[1]
                loss = criterion(outputs, labels)

                # Backward and optimize
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            if (epoch+1) % 100 == 0:
                print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.18f}')

        print(f'Final loss: {loss.item():.18f}')

        data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
        }

        FILE = self.outpath
        torch.save(data, FILE)

        print(f'Training complete. File saved to {FILE}')
