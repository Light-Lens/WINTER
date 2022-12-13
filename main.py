from src.AOs import AOs
from src.core import Speak, Listen
from src.alphabet import Classify, NLC
from colorama import Fore, Style, init

# initalize
CMD = AOs()
Nlc = NLC()
init(autoreset = True)

Classifier = Classify("models\\intents.json", "models\\data.pth")
Classifier.initalize()

# main code
print(f"{Fore.BLUE}{Style.BRIGHT}WINTER")
def main(text):
    print(f"> {text}")
    input_list = CMD.formatter(text)
    Prediction = [[i, list(Classifier.get_response( " ".join(i) ))] for i in input_list]

    for i in Prediction:
        txt, tag, responses = i[0], i[1][0], i[1][1]

        if tag == "default" or tag == "chat": topics = [" ".join(txt)]
        else:
            nlc = Nlc.predict(txt)
            topics = [" ".join(i) for i in CMD.formatter(nlc, nlc.split())]

        CMD.interpreter(tag, topics, responses)
        Speak(CMD.output)
