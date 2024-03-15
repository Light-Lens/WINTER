from src.vendor.GATw.src.alphabet.classification.train import Train
from src.vendor.GATw.src.alphabet.classification.sample import Sample

t = Train(
    n_layer = 8,
    n_hidden = 8,
    lr = 1e-3,
    batch_size = 32,
    model = "RNN"
)
t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=0.5)
t.train(
    n_steps = 4000,
    eval_interval = 400,
    eval_iters = 800
)
t.save("bin\\skills.pth")

s = Sample("bin\\skills.pth")
s.load()
print(s.predict("mute"))
print(s.predict("unmute"))
