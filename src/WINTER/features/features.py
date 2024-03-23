import json, func

class Features:
    def __init__(self, filepath):
        """
        @param filepath: the location of the json file.
        """

        with open(filepath, "r", encoding="utf-8") as f:
            self.jsondata = json.load(f)

    def load(self):
        self.func_dict = {
            "play,video": func.play_video,
            "play,music": func.play_music,
            "open,game": func.playgames,
            "play,on_youtube": func.youtube
        }

    # There are 3 execution engines: AOs, func, and skills.
    def execute(self, predicted_output):
        classname = predicted_output[0].split(";")[0]
        skillname = predicted_output[0].split(";")[1]
        score = predicted_output[1]

        for intent in self.jsondata[classname]:
            if skillname == intent["skill"]:
                execution_engine = intent["execution_engine"]
                task = intent["task"]
                break

        if execution_engine == None:
            pass

        # The AOs execution engine will execute tasks on AOs.
        elif execution_engine == "AOs":
            pass

        # The func execution engine will execute tasks on the functions written in for WINTER.
        elif execution_engine == "func":
            pass

        # The skills execution engine will execute a the task of a particular skill.
        elif execution_engine == "skills":
            pass

        else:
            pass
