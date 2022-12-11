from src.alphabet import Train

def init():
    # T1 = Train("models\\and.json", "models\\and.pth")
    # T1.initalize()

    # T2 = Train("models\\nlp.json", "models\\nlp.pth")
    # T2.initalize()

    T3 = Train("models\\intents.json", "models\\data.pth")
    T3.batch_size = 521
    T3.hidden_size = 521
    T3.initalize()

if __name__ == "__main__":
    init()
