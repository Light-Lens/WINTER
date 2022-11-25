from src.AOs import AOs
from src.alphabet import Classify, Train
from src.core import Speak, Listen

# Trainer = Train("models\\intents.json", "models\\data.pth")
# Trainer.initalize()

# Classifier = Classify("models\\data.pth", "models\\intents.json")
# Classifier.initalize()
# Prediction = Classifier.get_response("Play a mere hi liye")
# print(Prediction)

# Shell = AOs()
# Shell.input = ""
# Shell.interpreter()
# Shell.output

# Speak("Hello world!")
print(Listen())
