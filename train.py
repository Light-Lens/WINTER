from src.vendor.GATw.src.alphabet.classification.train import Train

t = Train(
    n_layer = 4,
    n_hidden = 8,
    lr = 1e-4,
    batch_size = 64,
    model = "RNN"
)
t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=None)
t.train(
    n_steps = 7000,
    eval_interval = 350,
    eval_iters = 700,
    n_loss_digits = 7
)
t.save("bin\\skills.pth")
