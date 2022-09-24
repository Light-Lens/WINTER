from assets.nltk_utils import bag_of_words, tokenize
from assets.model import NeuralNet
import json, torch

class Classify:
    def __init__(self, FILE, JSON):
        self.FILE = FILE
        self.JSON = JSON

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
        if confidence > 0.90:
            for intent in self.intents['intents']:
                response = intent['responses']
                if tag == intent["tag"]: return response

        else: return input_sent
