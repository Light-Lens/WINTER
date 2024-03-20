from src.vendor.GATw.src.alphabet.classification.train import Train

t = Train(
    n_layer = 3,
    n_hidden = 8,
    lr = 1e-3,
    batch_size = 32,
    model = "RNN"
)
t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=None)
t.train(
    n_steps = 2000,
    eval_interval = 200,
    eval_iters = 400
)
t.save("bin\\skills.pth")
