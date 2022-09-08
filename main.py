# WINTER
import speech_recognition as sr, pyttsx3, sys
from colorama import Fore, Style, init
from alphabet import ArrangeWords
from classify import Classify
from functions import *

# init modules
init(autoreset = True)

# TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id) # Ivona's Brian voice

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

def Speak(audio):
    if audio:
        print(audio)
        engine.say(audio)
        engine.runAndWait()

# Listen to the microphone and return a speech to text
def TakeCommand():
    print("> ", end="")
    with sr.Microphone() as source: audio = recognizer.listen(source, phrase_time_limit=4)
    try:
        Query = recognizer.recognize_google(audio, language = 'en-in')
        print(Query)

    except Exception as e:
        print()
        return ""

    return Query

# w2 is a class stands for write2 is a dialogue management system which will learn overtime.
class w2:
    def __init__(self, sentence):
        self.sentence = sentence

# Setup terminal
print(f"{Fore.BLUE}{Style.BRIGHT}WINTER")
ChatClassifier = Classify("pth\\chat.pth", "intents\\Chats.json")
ChatClassifier.initalize()

FuncClassifier = Classify("pth\\func.pth", "intents\\Func.json")
FuncClassifier.initalize()

while True:
    # Take input from the user and do some natural language processing on it.
    # Command = Core.TakeCommand().lower().strip()
    Command = input("> ").lower().strip()
    if Command == "exit": sys.exit()

    Func = FuncClassifier.get_response(Command)
    print(list(Func["responses"]))
    print(Func["confidence"])

    Chat = ChatClassifier.get_response(Command)
    print(ArrangeWords(list(Chat["responses"])))
    print(Chat["confidence"])
