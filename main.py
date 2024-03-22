from src.vendor.GATw.src.alphabet.classification.sample import Sample
from src.WINTER.core.features import Features

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
    "aalkjsdflkja9ierfasdfjlkaj adjfkkladjsfkl",
    "You know WINTER, my system has two button. One for sleep and the other one is for lock. No matter what you choose, they will perform the same function. Try it if you want.",
    "Lock this PC",
    "ya would you please put my system on sleep I'm going away for some time actually.",
    "please put my PC a lock. I won't be here."
]

f = Features("data\\skills.json")

for i in test:
    print(i)

    out = s.predict(i)

    classname = out[0].split(";")[0]
    tagname = out[0].split(";")[1]

    print(tagname, out[1])
    f.execute(classname, tagname)

    print()
