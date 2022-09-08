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

    def error(self, what_failed_todo=[]):
        # T1, T2: Template
        T1 = [["I'm", "I am", 3], ["Sorry"], ["sir", 5], ["but", 8]]
        T2 = [["I", 1], ["failed to", "wasn't able to", "couldn't"], what_failed_todo]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)
        S2 = ArrangeWords(T2)
        # Final_sent = " ".join([S1, S2]) if S1.endswith("but") else " ".join([S1, S2]) if random.randint(0, 8) > 4 else S1

        if S1.endswith("but"): Final_sent = " ".join([S1, S2])
        else:
            randnum = random.randint(0, 8)
            Final_sent = " ".join([S1, S2]) if randnum > 4 else S1

        Final_sent = " ".join([Final_sent, "sir."]).capitalize() if "sir" not in Final_sent and random.randint(0, 8) > 4 else Final_sent.capitalize()
        return Final_sent

# Setup terminal
print(f"{Fore.BLUE}{Style.BRIGHT}WINTER")
ChatClassifier = Classify("pth\\chat.pth", "intents\\Chats.json")
ChatClassifier.initalize()

FuncClassifier = Classify("pth\\func.pth", "intents\\Func.json")
FuncClassifier.initalize()
WINTER = w2("WINTER", "Male")

while True:
    # Take input from the user and do some natural language processing on it.
    # Command = Core.TakeCommand().lower().strip()
    Command = input("> ").lower().strip()
    out = {}

    Func = FuncClassifier.get_response(Command)
    Chat = ChatClassifier.get_response(Command)

    FuncResponse = str(Func["responses"][0])
    FuncConfidence = Func["confidence"]

    ChatResponse = ArrangeWords(list(Chat["responses"]))
    ChatConfidence = Chat["confidence"]

    responses_to_choose = {FuncResponse: FuncConfidence, ChatResponse: ChatConfidence}
    final_response = max(responses_to_choose, key=responses_to_choose.get)

    if final_response == "Exit":
        Template = [["Bye", "Sure", "As you wish", 4], ["Sir", 4]]

        Speak(ArrangeWords(Template))
        sys.exit()

    elif final_response == "Facts": out = Facts()
    elif final_response == "GetTime": out = GetTime()
    elif final_response == "GreetUs": out = GreetUs()
    elif final_response == "WeatherReport": out = WeatherReport()
    elif final_response == "TempReport": out = WeatherTemp()
    elif final_response == "CrackJokes": out = CrackJokes()
    elif final_response == "CreateProject": out = CreateProject(Command)
    elif final_response == "KillTask": out = KillTask(Command)
    elif final_response == "SearchOnline": out = SearchOnline(Command)
    elif final_response == "Summarize": out = Summarize(Command)
    elif final_response == "Translate": out = Translate(Command)
    elif final_response == "SwitchWindows": out = SwitchWindows(Command)
    elif final_response == "OpenSitesOrApps": out = OpenSitesOrApps(Command)
    elif final_response == "PlayOnYT": out = PlayOnYT(Command)
    elif final_response == "PlayOfflineMedia": out = PlayOfflineMedia(Command)
    else: out = final_response

    print(WINTER.error(["follow your query"]))
