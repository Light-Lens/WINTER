from src.vendor.GATw.src.alphabet.classification.train import Train

t = Train(
    n_layer = 4,
    n_hidden = 8,
    lr = 1e-4,
    batch_size = 64,
    model = "RNN"
)
t.preprocess("data\\skills.json", metadata=("skills", "skill", "patterns"), data_division=None, data_augmentation = 0.4)
t.train(
    n_steps = 20000,
    eval_interval = 200,
    eval_iters = 2000,
    n_loss_digits = 7
)
t.save("bin\\skills.pth")
