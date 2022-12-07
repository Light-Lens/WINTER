# Core
import speech_recognition as sr, pyttsx3, os

# TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id) #! Causing problem (Changing directory) ~> Solved
ROOT_DIR = os.path.dirname(os.path.normpath(  os.path.dirname(os.path.abspath(__file__))  ))

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

# Speak out loud the text
def Speak(audio):
    if not audio: return

    print(audio)
    engine.say(audio)
    engine.runAndWait()

    if os.getcwd() != ROOT_DIR: os.chdir(ROOT_DIR) #* Solution to the changing directory problem.

# Listen to the microphone and return a speech to text
def Listen():
    print("> ", end="")

    output = ""
    while not output:
        try:
            with sr.Microphone() as source: audio = recognizer.listen(source, phrase_time_limit=4)

            query = recognizer.recognize_google(audio, language = 'en-in')
            output = query.lower().strip()
            print(output)

        except KeyboardInterrupt: return ""
        except Exception: output = ""
    return output
