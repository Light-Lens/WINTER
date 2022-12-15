from colorama import Fore, Style, init
from src.core import Speak, Listen
from src.models.rpa.aos import aos
from src.models.lang.alphabet import Train

# Train class
def train_all():
    # T1 = Train()
    T2 = Train(outpath="models\\and.pth", intentclass="and")
    # T3 = Train(outpath="models\\or.pth", intentclass="and")
    # T4 = Train(outpath="models\\nlp.pth", intentclass="nlp")

    T2.hidden_size = 4

    # T1.init()
    T2.init()
    # T3.init()
    # T4.init()

# initalize
AOs = aos()
# train_all()
init(autoreset = True)

# main code
print(f"{Fore.BLUE}{Style.BRIGHT}WINTER")
text = ["open chrome and edge", "close this app and search how gpt 3 works", "tell me today's time and date", "lock pc and subtract 2 - 2",
"take all windows down and update my pc", "open sublime text 3 and get rid of this app", "this is just a text and open chrome",
"restart my pc and remember to calibrate the venv", "you know I was studying a topic and it was very interesting", "I studied atoms last night and search on google for what is a game engine",
"search on google for what is a game engine and how does it work"]

for i in text:
    input_list = AOs.formatter(i)
    print(input_list)
