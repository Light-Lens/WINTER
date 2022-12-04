from src.alphabet import Train

def init():
    T1 = Train("models\\intents.json", "models\\data.pth")
    T1.initalize()

    # T2 = Train("models\\and.json", "models\\and.pth")
    # T2.num_epochs = 2000
    # T2.initalize()

    # T3 = Train("models\\nlp.json", "models\\nlp.pth")
    # T3.num_epochs = 1000
    # T3.initalize()

if __name__ == "__main__":
    init()
