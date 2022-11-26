import re
from src.AOs import AOs
from src.core import Speak, Listen
from src.alphabet import Classify, Train
from src.nltk_utils import NormalizeSent

Shell = AOs()

intentspath, datapath = "models\\intents.json", "models\\data.pth"
Trainer = Train(intentspath, datapath)
Classifier = Classify(intentspath, datapath)

# Trainer.initalize()
Classifier.initalize()

# Shell.input = Listen()
Shell.input = "tell me a fact and a joke and today's weather and open sublime text for me, please and create project mark it mark 5"
input_list = [" ".join(i) for i in Shell.formatter()]
Prediction = [Classifier.get_response(i) for i in input_list]

tokens = []
lis = dict(zip(Prediction, input_list))
for i in lis:
    tokens.append([])
    sent = NormalizeSent(lis[i])
    if i == "exit": tokens[-1].append("exit")
    elif i == "lock": tokens[-1].append("lock")
    elif i == "restart": tokens[-1].append("restart")
    elif i == "shutdown": tokens[-1].append("shutdown")

    elif i == "time": tokens[-1].append("time")
    elif i == "date": tokens[-1].append("date")
    elif i == "greet": tokens[-1].append("greet")
    elif i == "temp": tokens[-1].append("temp")
    elif i == "joke": tokens[-1].append("joke")
    elif i == "fact": tokens[-1].append("fact")
    elif i == "weather": tokens[-1].append("weather")
    elif i == "open":
        regex = re.findall(r'(?:start|launch|open)\s+(.*)', sent)

        tokens[-1].append(i)
        tokens[-1].append(regex[0] if regex else "")

    elif i == "create":
        regex = re.findall(r'(?:project)\s+(.*)', sent)
        regex2 = re.findall(r'(?:indexed|named|marked|mark)\s+(.*)', ( regex[0] if regex else "" ))

        tokens[-1].append(i)
        tokens[-1].append(regex2[0] if regex2 else "")

print(tokens)
