# Core
import speech_recognition as sr, pyttsx3, asyncio, edge_tts, os
from playsound import playsound

# Speech recognizer
recognizer = sr.Recognizer()
recognizer.pause_threshold = 1

# Speak out loud the text
def Speak(text, voice="en-US-GuyNeural"):
    output = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp", "audio.mp3")

    # TTS engine
    async def _main(text, voice) -> None:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(_main(text, voice))

    print(text)
    playsound(os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp", "audio.mp3"))

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

#? This is the old speak function using pyttsx3. [NOTE: Is is usefull for offline use.]
# ROOT_DIR = os.path.dirname(os.path.normpath(os.path.dirname(os.path.abspath(__file__))))
# def Speak(audio):
#     if not audio: return

#     # TTS engine
#     print(audio)
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('rate', 180)
#     engine.setProperty('voice', voices[0].id) #! Causing problem (Changing directory) ~> Solved
#     engine.say(audio)
#     engine.runAndWait()

#     if os.getcwd() != ROOT_DIR: os.chdir(ROOT_DIR) #* Solution to the changing directory problem.
