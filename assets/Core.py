# Core
import speech_recognition as sr, pyttsx3, random, sys
from alphabet import ArrangeWords

# TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id) # Ivona's Brian voice

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

# Speak out loud the text
def Speak(audio):
    if audio:
        print(audio)
        engine.say(audio)
        engine.runAndWait()

# Listen to the microphone and return a speech to text
def TakeCommand():
    Output = ""
    print("> ", end="")
    while not Output:
        try:
            with sr.Microphone() as source: audio = recognizer.listen(source, phrase_time_limit=4)

        except KeyboardInterrupt: sys.exit()

        try:
            Query = recognizer.recognize_google(audio, language = 'en-in')
            Output = Query.lower().strip()
            print(Output)

        except sr.RequestError: Output = input().lower().strip()
        except Exception: Output = ""
    return Output

# w2 is a class stands for write2 is a dialogue management system which will learn overtime.
class w2:
    # This init function will keep some bot details for future use.
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @staticmethod
    def add_sir(sentence):
        Final_sent = sentence.replace(", ", " sir, ") if random.randrange(9) > 4 else sentence

        # Final touches to the generated sentence
        for i in [".", "?", "!"]:
            if Final_sent.endswith(i):
                Final_sent = " ".join([Final_sent, f"sir{i}"]) if not Final_sent.endswith(i) and random.randrange(9) > 4 and "sir" not in Final_sent.lower() else Final_sent
                Final_sent = " ".join([Final_sent[:-1], f"sir{i}"]) if Final_sent.endswith(i) and random.randrange(9) > 4 and "sir" not in Final_sent.lower() else Final_sent
                break

        Final_sent + "." if not any(Final_sent.endswith(i) for i in [".", "?", "!"]) else Final_sent
        return Final_sent

    @staticmethod
    def assure():
        # T1: Template
        T1 = [["Yup", "Very well", "Right on", "Alright", "For sure", "By all means", "Always", "You're on", "Yes",
                "Yep", "Yeah", "Of course", "Affirmative", "Sure", "Ok", "Okay", "As you wish", "Here you go",
                "No problem", "Right away", "Sure, no problem", "Ok, no problem", "Okay, no problem"]]

        # S1: Sentence
        S1 = ArrangeWords(T1)
        return S1.capitalize() + "."

    @staticmethod
    def error(what_failed_todo=[]):
        # T1, T2: Template
        T1 = [["I'm", "I am", 3], ["Sorry"], ["sir", 5], ["but", 8]]
        T2 = [["I", 1], ["failed to", "wasn't able to", "couldn't"], what_failed_todo]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)
        S2 = ArrangeWords(T2)

        # Final touches to the generated sentence
        Final_sent = " ".join([S1, S2]) if S1.lower().endswith("but") else " ".join([S1, S2]) if random.randrange(9) > 4 else S1
        return Final_sent.capitalize() + "."
