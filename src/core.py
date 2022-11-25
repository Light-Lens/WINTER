# Core
import speech_recognition as sr, pyttsx3

# TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[0].id)

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

# Speak out loud the text
def speak(audio):
    if not audio: return

    print(audio)
    engine.say(audio)
    engine.runAndWait()

# Listen to the microphone and return a speech to text
def listen():
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
