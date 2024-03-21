from src.vendor.GATw.src.alphabet.classification.sample import Sample

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
    "pronto, I want you to set the volume slider to sixty nine."
]

for i in test:
    print(i)
    print(s.predict(i))
    print()
