from src.AOs import AOs
from src.core import Speak, Listen
from src.alphabet import Classify, NLC
from src.nltk_utils import ArrangeWords

# initalize
CMD = AOs()
Nlc = NLC()

Classifier = Classify("models\\intents.json", "models\\data.pth")
Classifier.initalize()

# main code
text = "please give me the summary of steve jobs' life"
input_list = CMD.formatter(text)
Prediction = [[i, list(Classifier.get_response( " ".join(i) ))] for i in input_list]

for i in Prediction:
    text, tag, response = i[0], i[1][0], i[1][1]
    topic = Nlc.predict(text)

    # Speak(ArrangeWords(response))
    print([tag, topic])
