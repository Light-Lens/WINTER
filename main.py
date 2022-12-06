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
text = "can you search on google about google chrome and tell me the time"
input_list = CMD.formatter(text)
Prediction = [[i, list(Classifier.get_response( " ".join(i) ))] for i in input_list]

for i in Prediction:
    text, tag, response = i[0], i[1][0], i[1][1]
    nlc = Nlc.predict(text)
    topics = [" ".join(i) for i in CMD.formatter(nlc, nlc.split())]

    # Speak(ArrangeWords(response))
    print([tag, topics])
