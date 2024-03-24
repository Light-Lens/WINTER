# https://github.com/davabase/whisper_real_time.git
import speech_recognition as sr
from datetime import datetime, timedelta
from queue import Queue
from time import sleep
import numpy as np
import os

from colorama import Style, Fore, init

# import colorama module to differentiate between speech output and error
init(True)

# We use SpeechRecognizer to record our audio
# because it has a nice feature where it can detect when speech ends.
recorder = sr.Recognizer()
# recorder.pause_threshold = 0.02
recorder.energy_threshold = 1000 # change accordingly.
# Definitely do this, dynamic energy compensation lowers the energy threshold dramatically
# to a point where the SpeechRecognizer never stops recording.
recorder.dynamic_energy_threshold = False

# # Listen to the microphone and return a speech to text
# def Listen():
#     output = ""
#     while not output:
#         try:
#             with sr.Microphone(sample_rate=16000) as source:
#                 recorder.adjust_for_ambient_noise(source)
#                 audio = recorder.listen(source, phrase_time_limit=2)

#             output = recorder.recognize_google(audio, language='en-in')

#         except KeyboardInterrupt:
#             return output

#         except Exception as e:
#             print(f"{Style.BRIGHT}{Fore.RED}{e}")
#             output = ""

#     return output

record_timeout = 2
phrase_timeout = 3
# The last time a recording was retrieved from the queue.
phrase_time = None

source = sr.Microphone(sample_rate=16000)

transcription = ['']

# Thread safe Queue for passing data from the threaded recording callback.
data_queue = Queue()

with source:
    recorder.adjust_for_ambient_noise(source)

def record_callback(_, audio:sr.AudioData) -> None:
    """
    Threaded callback function to receive audio data when recordings finish.
    audio: An AudioData containing the recorded bytes.
    """
    # Grab the raw bytes and push it into the thread safe queue.
    data_queue.put(audio)

# Create a background thread that will pass us raw audio bytes.
# We could do this manually but SpeechRecognizer provides a nice helper.
recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)

# Cue the user that we're ready to go.
print("Model loaded.\n")

while True:
    try:
        now = datetime.utcnow()
        # Pull raw recorded audio from the queue.
        if not data_queue.empty():
            phrase_complete = False
            # If enough time has passed between recordings, consider the phrase complete.
            # Clear the current working audio buffer to start over with the new data.
            if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                phrase_complete = True
            # This is the last time we received new audio data from the queue.
            phrase_time = now

            # Read the transcription.
            text = " ".join([recorder.recognize_google(audio_data, language="en-in") for audio_data in data_queue.queue])
            data_queue.queue.clear()

            # If we detected a pause between recordings, add a new item to our transcription.
            # Otherwise edit the existing one.
            if phrase_complete:
                transcription.append(text)
            else:
                transcription[-1] = text

            # Clear the console to reprint the updated transcription.
            os.system('cls' if os.name=='nt' else 'clear')
            for line in transcription:
                print(line)
            # Flush stdout.
            print('', end='', flush=True)
        else:
            # Infinite loops are bad for processors, must sleep.
            sleep(0.25)
    except KeyboardInterrupt:
        break

print("\n\nTranscription:")
for line in transcription:
    print(line)
