from src.alphabet import Train

def init():
    T1 = Train("models\\and.json", "models\\and.pth")
    T2 = Train("models\\nlp.json", "models\\nlp.pth")
    T3 = Train("models\\intents.json", "models\\data.pth")

    T2.batch_size = 32
    T2.hidden_size = 128

    T1.initalize()
    T2.initalize()
    T3.initalize()

if __name__ == "__main__":
    init()
