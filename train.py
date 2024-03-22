from src.vendor.GATw.src.alphabet.classification.train import Train

t = Train(
    n_layer = 4,
    n_hidden = 16,
    lr = 4e-3,
    batch_size = 64,
    model = "RNN"
)
t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=None)
t.train(
    n_steps = 2000,
    eval_interval = 200,
    eval_iters = 800,
    n_loss_digits = 7
)
t.save("bin\\skills.pth")
