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
        # There are 3 execution engines.
        # AOs, func, and skills.
        # The AOs execution engine will execute tasks on AOs.
        # The func execution engine will execute tasks on the functions written in for WINTER.
        # The skills execution engine will execute a the task of a particular skill.

        for intent in self.jsondata[classname]:
            if skillname == intent["skill"]:
                execution_engines = intent["execution_engine"]
                task = intent["task"]
                break

        print(execution_engines)
        print(task)
