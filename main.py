from colorama import Fore, Style, init
from src.core import Speak, Listen
from src.models.rpa.aos import aos
from src.models.lang.alphabet import Classify, Train, nlc

# Train class
def train_all():
    T1 = Train()
    T2 = Train(outpath="models\\and.pth", intentclass="and")
    T3 = Train(outpath="models\\wake.pth", intentclass="wake up")
    T4 = Train(outpath="models\\stopwords.pth", intentclass="stopwords")

    T1.hidden_size = 32
    T3.hidden_size = 4
    T4.hidden_size = 16

    T1.init()
    T2.init()
    T3.init()
    T4.init()

# initalize
train_all()
AOs = aos()
NLC = nlc()
init(autoreset = True)

Classifier = Classify()
Classifier.init()

# main code
print(f"{Fore.BLUE}{Style.BRIGHT}WINTER")
text = ["open chrome and start minecraft", "close this app and search how gpt 3 works", "tell me today's time and date", "lock pc and subtract 2 - 2",
"take all windows down and update my pc", "open sublime text 3 and get rid of this app", "this is just a text and open chrome",
"restart my pc and remember to calibrate the venv", "you know I was studying a topic and it was very interesting",
"I studied atoms last night and search on google for what is a game engine", "search on google for what is a game engine and how does it work",
"start a project and mark it as Atomic Intelligence", "can you divide 3/0"]

for i in text:
    input_list = AOs.formatter(i)
    # Prediction = [Classifier.predict(" ".join(i)) for i in input_list]
    # print(Prediction, [" ".join(i) for i in input_list])
    print([" ".join(i) for i in input_list])
    print([" ".join(NLC.predict(i)) for i in input_list])
