from . import func
import json

class Features:
    def __init__(self, filepath):
        """
        @param filepath: the location of the json file.
        """

        self.func_dict = {}

        with open(filepath, "r", encoding="utf-8") as f:
            self.jsondata = json.load(f)

    def load(self):
        self.func_dict = {
            "play,video": func.play_video,
            "play,music": func.play_music,
            "open,game": func.playgames,
            "play,on_youtube": func.youtube,
            "search,wikipedia": func.search_on_wikipedia,
            "translate,one_lang_to_another": func.translate
        }

    # There are 3 execution engines: AOs, func, and skills.
    def execute(self, predicted_output):
        classname = predicted_output[0].split(";")[0]
        skillname = predicted_output[0].split(";")[1]
        score = predicted_output[1]

        if score < 0.7:
            # The "default" skill states that the particular input is actually a conversation rather than a intent.
            skillname = "default"
            score = 1

        for intent in self.jsondata[classname]:
            if skillname == intent["skill"]:
                tasks = intent["tasks"]
                responses = intent["responses"]
                response_config = intent["response_config"]
                break

        self.__give_response__(responses, response_config)
        self.__exec_tasks__(tasks, skillname)

    def __give_response__(self, responses, response_config):
        pass

    def __exec_tasks__(self, tasks, skillname):
        for task in tasks:
            cmd = task["cmd"]
            args = task["args"]
            exec_engine = task["execution_engine"]

            print(cmd, args, exec_engine)

            if exec_engine == None:
                pass

            elif exec_engine == "func":
                if skillname in self.func_dict.keys():
                    print(args)
                    # self.func_dict[skillname]()

            elif exec_engine == "AOs":
                pass

            elif exec_engine == "skills":
                pass
 