# WINTER
from colorama import Fore, Style, init
from assets.alphabet import ArrangeWords
from assets.classify import Classify
from assets.CMD import cmd
from assets.Core import *
import nltk

# TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id) # Ivona's Brian voice

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

# Download nltk library
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('nps_chat')
# nltk.download('stopwords')

# init modules
init(autoreset = True)

# Setup terminal
WINTER = w2("WINTER", "Male")
print(f"{Fore.BLUE}{Style.BRIGHT}{WINTER.name}")

Classifier = Classify("data\\scripts\\data.pth", "data\\scripts\\intents.json")
Classifier.initalize()
while True:
    # Take input from the user and do some natural language processing on it.
    try: Command = input("> ").lower().strip()
    except KeyboardInterrupt: sys.exit()
    # Command = TakeCommand()

    Features = ["OpenSitesOrApps", "KillTask", "SwitchWindows", "ShutdownPC", "RestartPC", "PlayOnYT",
                "PlayOfflineMedia", "SearchOnline", "SearchOnline", "LockPC", "CreateProject", "WeatherReport",
                "TempReport", "Translate", "CrackJokes", "Facts", "CalcMath", "GetTime"]

    Prediction = Classifier.get_response(Command)
    # Prediction = ArrangeWords(Prediction) if not isinstance(Prediction, str) else Prediction

    if not isinstance(Prediction, str):
        Speak(w2.add_sir(ArrangeWords(Prediction)))

    else:
        try: eval(f"cmd.{Prediction}(Command)")
        except Exception: eval(f"cmd.{Prediction}()")
