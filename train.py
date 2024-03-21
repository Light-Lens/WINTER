from src.vendor.GATw.src.alphabet.classification.train import Train

t = Train(
    n_layer = 4,
    n_hidden = 8,
    lr = 4e-3,
    batch_size = 64,
    model = "RNN"
)
t.preprocess(
    filepath = "data\\skills.json",
    metadata = ("skills", "skill", "patterns"),
    data_division = 0.8,
    data_augmentation = 0.4
)

t.train(
    n_steps = 10000,
    eval_interval = 200,
    eval_iters = 2000,
    n_loss_digits = 7
)
t.save("bin\\skills.pth")
