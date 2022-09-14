# WINTER
import speech_recognition as sr, pyttsx3, random, sys
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

# Download nltk library
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('nps_chat')
# nltk.download('stopwords')

# Speak out loud the text.
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
    # This init function will keep some bot details for future use.
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.vocabulary = list(set([]))

    def generate(self, sentence):
        self.vocabulary

    def follow_up_questions(self, topic):
        self.vocabulary

    def add_sir(self, sentence):
        Final_sent = sentence.replace(", ", " sir, ") if random.randrange(9) > 4 else sentence

        # Final touches to the generated sentence
        for i in [".", "?", "!"]:
            if Final_sent.endswith(i):
                Final_sent = " ".join([Final_sent, f"sir{i}"]) if not Final_sent.endswith(i) and random.randrange(9) > 4 and "sir" not in Final_sent.lower() else Final_sent
                Final_sent = " ".join([Final_sent[:-1], f"sir{i}"]) if Final_sent.endswith(i) and random.randrange(9) > 4 and "sir" not in Final_sent.lower() else Final_sent
                break

        Final_sent + "." if not any(Final_sent.endswith(i) for i in [".", "?", "!"]) else Final_sent
        return Final_sent

    def assure(self):
        # T1: Template
        T1 = [["Yup", "Very well", "Right on", "Alright", "For sure", "By all means", "Always", "You're on", "Yes",
                "Yep", "Yeah", "Of course", "Affirmative", "Sure", "Ok", "Okay", "As you wish", "Here you go",
                "No problem", "Right away", "Sure, no problem", "Ok, no problem", "Okay, no problem"], ["sir", 8]]

        # S1: Sentence
        S1 = ArrangeWords(T1)
        return S1.capitalize() + "."

    def error(self, what_failed_todo=[]):
        # T1, T2: Template
        T1 = [["I'm", "I am", 3], ["Sorry"], ["sir", 5], ["but", 8]]
        T2 = [["I", 1], ["failed to", "wasn't able to", "couldn't"], what_failed_todo]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)
        S2 = ArrangeWords(T2)

        # Final touches to the generated sentence
        Final_sent = " ".join([S1, S2]) if S1.lower().endswith("but") else " ".join([S1, S2]) if random.randrange(9) > 4 else S1
        Final_sent = " ".join([Final_sent, "sir."]) if "sir" not in Final_sent.lower() and random.randrange(9) > 4 else Final_sent

        return Final_sent.capitalize() + "."

# Setup terminal
WINTER = w2("WINTER", "Male")
print(f"{Fore.BLUE}{Style.BRIGHT}{WINTER.name}")

Classifier = Classify("data.pth", "intents.json")
Classifier.initalize()

TestCommands = ["wake up", "hello", "how are you", "hello how are you", "what are you doing", "you here",
                "you there", "how are we doing", "bye", "exit", "facts", "time", "morning", "i want to listen a joke",
                "weather", "solve the problem 2 + 5", "play mere hi liye", "play mere hi liye on youtube",
                "play a song", "show me a picture", "give me a summary on steve jobs", "translate tum kaise ho",
                "search what is deep learning", "start a new project indexed as mark 5", "switch", "open google"]

for Command in TestCommands:
# while True:
    # Take input from the user and do some natural language processing on it.
    # Command = TakeCommand().lower().strip()
    # Command = input("> ").lower().strip()

    print(">", Command)
    Prediction = Classifier.get_response(Command)
    Prediction = ArrangeWords(Classifier.get_response(Command)) if not isinstance(Prediction, str) else Prediction
    Prediction = WINTER.add_sir(Prediction)

    print(Prediction, end="\n"*2)
    WINTER.vocabulary.append(Prediction)

print(f"{WINTER.vocabulary}")
