from src.vendor.GATw.src.alphabet.classification.sample import Sample
from src.WINTER.src.utils.dprint import dprint
import json

s = Sample("bin\\skills.pth")
s.load()

test = [
    "please make the volume one hundred percent.",
    "turn the volume to zero percent.",
    "I think that things won't be any perfect than a quite PC",
    "I think that things won't be any perfect than a quite PC. Mute this device please.",
    "I don't think that things won't be any perfect than a quite PC.",
    "set volume one hundred percent.",
    "set the volume to zero percent.",
    "mute my pc for a minute",
    "unmute my PC now.",
    "increase the volume of this PC.",
    "please increase the volume",
    "please increase the volume by ten percent.",
    "please reduce the volume by fifteen points.",
    "set volume fifty nine",
    "pronto, I want you to set the volume slider to sixty nine.",
    "aalkjsdflkja9ierfasdfjlkaj adjfkkladjsfkl"
]

with open("data\\skills.json", 'r', encoding='utf-8') as f:
    jsondata = json.load(f)

for i in test:
    print(i)

    out = s.predict(i)
    score = out[1]
    classname = out[0].split(";")[0]
    tagname = out[0].split(";")[1]

    if score >= 0.8:
        for intent in jsondata[classname]:
            if tagname == intent["skill"]:
                # Shuffle the responses list based on a seed and print the results one-by-one not randomly.
                # Keep track the index of the last response and print the following response.
                print(tagname, score)
                print(f"response: {intent['responses'][0]}")
                print(intent["task"], intent["execution_engine"])
                print()

    else:
        #* Temporary response when no intent matches the score of 80%.
        # Make it more robust and give differnt responses each time.
        # Keep track the index of the last response and print the following response.
        dprint("Sorry, but I can't understand you :(")
