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
    # Command = input("> ").lower().strip()
    Command = TakeCommand()

    Features = ["OpenSitesOrApps", "KillTask", "SwitchWindows", "ShutdownPC", "RestartPC", "PlayOnYT",
                "PlayOfflineMedia", "SearchOnline", "SearchOnline", "LockPC", "CreateProject", "WeatherReport",
                "TempReport", "Translate", "CrackJokes", "Facts", "CalcMath", "GetTime"]

    Prediction = Classifier.get_response(Command)
    Prediction = ArrangeWords(Prediction) if not isinstance(Prediction, str) else Prediction
    if Prediction == "OpenSitesOrApps": cmd.OpenSitesOrApps(Command)
    elif Prediction == "KillTask": cmd.KillTask(Command)
    elif Prediction == "SwitchWindows": cmd.SwitchWindows(Command)
    elif Prediction == "ShutdownPC": cmd.ShutdownPC()
    elif Prediction == "RestartPC": cmd.RestartPC()
    elif Prediction == "PlayOnYT": cmd.PlayOnYT(Command)
    elif Prediction == "PlayOfflineMedia": cmd.PlayOfflineMedia(Command)
    elif Prediction == "SearchOnline": cmd.SearchOnline(Command)
    elif Prediction == "LockPC": cmd.LockPC()
    elif Prediction == "CreateProject": cmd.CreateProject(Command)
    elif Prediction == "WeatherReport": cmd.WeatherReport()
    elif Prediction == "TempReport": cmd.TempReport()
    elif Prediction == "Translate": cmd.Translate(Command)
    elif Prediction == "CrackJokes": cmd.CrackJokes()
    elif Prediction == "Facts": cmd.Facts()
    elif Prediction == "CalcMath": cmd.CalcMath(Command)
    elif Prediction == "GetTime": cmd.GetTime()
    else: Speak(Prediction)
