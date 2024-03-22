import json

class Features:
    def __init__(self, filepath):
        """
        @param filepath: the location of the json file.
        """

        with open(filepath, "r", encoding="utf-8") as f:
            self.jsondata = json.load(f)

    def load_features(self):
        pass

    def execute(self, classname, skillname):
        for intent in self.jsondata[classname]:
            if skillname == intent["skill"]:
                execution_engines = intent["execution_engine"]
                task = intent["task"]
                break

        print(execution_engines)
        print(task)
