from src.vendor.GATw.src.alphabet.classification.train import Train
from src.vendor.GATw.src.alphabet.classification.sample import Sample

# t = Train(
#     n_layer = 2,
#     n_hidden = 8,
#     lr = 1e-3,
#     batch_size = 32,
#     model = "RNN"
# )
# t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=None)
# t.train(
#     n_steps = 1000,
#     eval_interval = 100,
#     eval_iters = 400
# )
# t.save("bin\\skills.pth")

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
    "unmute my PC now."
]

for i in test:
    print(i)
    print(s.predict(i))
    print()
