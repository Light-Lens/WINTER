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
        text, tag, responses = i[0], i[1][0], i[1][1]

        if tag == "default" or tag == "chat": topics = [" ".join(text)]
        else:
            nlc = Nlc.predict(text)
            topics = [" ".join(i) for i in CMD.formatter(nlc, nlc.split())]

        print(tag, topics)
        CMD.interpreter(tag, topics, responses)
        # Speak(CMD.output)

main("open sublime text")

# if __name__ == "__main__":
#     while True:
#         with open("assets\\current.txt") as f: text = f.read()
#         main(text) if text else None
