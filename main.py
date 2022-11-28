import re
from src.AOs import AOs
from src.core import Speak, Listen
from src.alphabet import Classify, Train
from src.nltk_utils import ClassifyIntent, NormalizeSent

Shell = AOs()

intentspath, datapath = "models\\intents.json", "models\\data.pth"
Trainer = Train(intentspath, datapath)
Classifier = Classify(intentspath, datapath)

# Trainer.initalize()
Classifier.initalize()

while True:
    # Shell.input = Listen()
    Shell.input = input("> ")
    input_list = [" ".join(i) for i in Shell.formatter()]
    Prediction = [Classifier.get_response(i) for i in input_list]

    tokens = []
    lis = dict(zip(Prediction, input_list))
    for i in lis:
        tokens.append([])
        sent = NormalizeSent(lis[i])
        if any(i == j for j in ["time", "date", "greet", "temp", "joke", "fact", "weather", "exit", "lock", "restart", "shutdown", "resizewindow"]):
            tokens[-1].append(i)

        elif i == "open":
            regex = re.findall(r'(?:start|launch|open)\s+(.*)', sent)
            r = regex[0] if regex else sent

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "play":
            regex = re.findall(r'song|video|picture|pic|music|movie', sent)
            r = regex[0] if regex else sent

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "close":
            regex = re.findall(r'(?:close|kill|quit|exit|shutdown)\s+(.*)', sent)
            r = regex[0] if regex else "current app"

            tokens[-1].append(i)
            score = ClassifyIntent(r, ["current tab", "current app", "this app", "this tab", "current window", "this window", "this window"])
            if score[0] > 0.8:
                if "tab" in score[1]: tokens[-1].append("_tab")
                elif "app" in score[1] or "window" in score[1]: tokens[-1].append("_currentapp")

            else: tokens[-1].append(r)

        elif i == "switch":
            regex = re.findall(r'(?:switch|change)\s+(.*)', sent)
            r = regex[0] if regex else "current app"

            tokens[-1].append(i)
            score = ClassifyIntent(r, ["current tab", "current app", "this app", "this tab", "current window", "this window", "this window"])
            if score[0] > 0.8:
                if "tab" in score[1]: tokens[-1].append("_tab")
                elif "app" in score[1] or "window" in score[1]: tokens[-1].append("_currentapp")

            else: tokens[-1].append(r)

        elif i == "create":
            regex = re.findall(r'(?:project)\s+(.*)', sent)
            regex2 = re.findall(r'(?:indexed|named|marked|mark)\s+(.*)', regex[0] if regex else sent)
            r = regex2[0] if regex2 else sent

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "youtube":
            regex = re.findall(r'(?:play|search)\s+(.*)', lis[i])
            regex2 = re.findall(r'youtube\s+(.*)', regex[0] if regex else lis[i])
            r = regex2[0] if regex2 else lis[i]

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "calc":
            regex = re.findall(r'(?:divide|multiply|add|subtract|minus|plus|times|evaluate|solve|calculate)\s+(.*)', sent)
            r = regex[0] if regex else sent

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "search":
            regex = re.findall(r'(?:wikipedia for|google for|search wikipedia|search google|search on wikipedia|search on google|search for|search on|search)\s+(.*)', lis[i])
            r = regex[0] if regex else lis[i]

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "summary":
            regex = re.findall(r'(?:summary on|summarize|summary of|summary)\s+(.*)', lis[i])
            r = regex[0] if regex else lis[i]

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "translate":
            regex = re.findall(r'(?:translate this to english|translate to english|translate this|translate)\s+(.*)', lis[i])
            r = regex[0] if regex else lis[i]

            tokens[-1].append(i)
            tokens[-1].append(r)

        elif i == "chat":
            tokens[-1].append(i)
            tokens[-1].append(lis[i])

    for i in tokens:
        Shell.interpreter(i)
        Speak(Shell.output)
