# WINTER
from Core import *
import subprocess

# Setup terminal
print(f"{Fore.BLUE}{Style.BRIGHT}{WINTER.name}")

Classifier = Classify("data.pth", "intents.json")
Classifier.initalize()
while True:
    # Take input from the user and do some natural language processing on it.
    Command = input("> ").lower().strip()
    # Command = TakeCommand()

    Prediction = Classifier.get_response(Command)
    # Prediction = ArrangeWords(Prediction) if not isinstance(Prediction, str) else Prediction
    if isinstance(Prediction, str): subprocess.call(["python", f"data\\cmd\\{Prediction}.py", Command])
    else:
        Prediction = ArrangeWords(Prediction)
        Speak(Prediction)
