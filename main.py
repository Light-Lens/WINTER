from src.vendor.GATw.src.write.train import Train
from src.vendor.GATw.src.write.sample import Sample

t = Train(
    n_layer = 4,
    n_embd = 16,
    n_head = 4,
    lr = 2e-3,
    dropout = 0,
    block_size = 128,
    batch_size = 32
)
t.preprocess("data\\LLM data.txt")
t.train(
    n_steps = 2000,
    eval_interval = 200,
    eval_iters = 400
)
t.save("bin\\GAT-w.pth")

s = Sample("bin\\GAT-w.pth")
s.load()
s.generate("How can we reduce air pollution?")


# from src.vendor.GATw.src.alphabet.classification.train import Train
# from src.vendor.GATw.src.alphabet.classification.sample import Sample

# t = Train(
#     n_layer = 3,
#     n_hidden = 8,
#     lr = 1e-3,
#     batch_size = 32,
#     model = "RNN"
# )
# t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=None)
# t.train(
#     n_steps = 2000,
#     eval_interval = 200,
#     eval_iters = 400
# )
# t.save("bin\\skills.pth")

# s = Sample("bin\\skills.pth")
# s.load()

# test = [
#     "please make the volume one hundred percent.",
#     "turn the volume to zero percent.",
#     "I think that things won't be any perfect than a quite PC",
#     "I think that things won't be any perfect than a quite PC. Mute this device please.",
#     "I don't think that things won't be any perfect than a quite PC.",
#     "set volume one hundred percent.",
#     "set the volume to zero percent.",
#     "mute my pc for a minute",
#     "unmute my PC now.",
#     "increase the volume of this PC.",
#     "please increase the volume"
# ]

# for i in test:
#     print(i)
#     print(s.predict(i))
#     print()
