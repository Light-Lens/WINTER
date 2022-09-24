#!/usr/bin/env python
# WINTER
from colorama import Fore, Style, init
from assets.alphabet import ArrangeWords
from assets.classify import Classify
from assets.protocol import Protocol
from assets.core import *
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

Classifier = Classify("data\\models\\data.pth", "data\\models\\intents.json")
Classifier.initalize()
while True:
    # Take input from the user and do some natural language processing on it.
    Command = input("> ").lower().strip()
    # Command = TakeCommand()

    Prediction = Classifier.get_response(Command)
    Prediction = ArrangeWords(Prediction) if not isinstance(Prediction, str) else Prediction
    if Prediction == "Exit": Protocol.Exit()
    elif Prediction == "OpenSitesOrApps": Protocol.OpenSitesOrApps(Command)
    elif Prediction == "KillTask": Protocol.KillTask(Command)
    elif Prediction == "SwitchWindows": Protocol.SwitchWindows(Command)
    elif Prediction == "ShutdownPC": Protocol.ShutdownPC()
    elif Prediction == "RestartPC": Protocol.RestartPC()
    elif Prediction == "PlayOnYT": Protocol.PlayOnYT(Command)
    elif Prediction == "PlayOfflineMedia": Protocol.PlayOfflineMedia(Command)
    elif Prediction == "SearchOnline": Protocol.SearchOnline(Command)
    elif Prediction == "LockPC": Protocol.LockPC()
    elif Prediction == "CreateProject": Protocol.CreateProject(Command)
    elif Prediction == "WeatherReport": Protocol.WeatherReport()
    elif Prediction == "TempReport": Protocol.TempReport()
    elif Prediction == "Translate": Protocol.Translate(Command)
    elif Prediction == "CrackJokes": Protocol.CrackJokes()
    elif Prediction == "Facts": Protocol.Facts()
    elif Prediction == "CalcMath": Protocol.CalcMath(Command)
    elif Prediction == "GetTime": Protocol.GetTime()
    else: Speak(Prediction)
