from ..shared.utils import dprint
from . import func
import random, json

class Features:
    def __init__(self, filepath):
        """
        @param filepath: the location of the json file.
        """

        self.filepath = filepath
        self.func_dict = {}

        with open(self.filepath, "r", encoding="utf-8") as f:
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

        intent["response_config"] = self.__give_response__(responses, response_config)
        self.__exec_tasks__(tasks, skillname)
        self.__update_response_config__()
        print(skillname, score)

    def __update_response_config__(self):
        # Serializing json
        json_obj = json.dumps(self.jsondata, indent=4)
        
        # Writing to sample.json
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(json_obj)

    def __give_response__(self, responses, response_config):
        enable_dprint = response_config["dprint"]
        shuffle = response_config["shuffle"]
        do_reverse = response_config["reverse"]
        shuffle_seed = response_config["shuffle_seed"]

        if (response_config["last_response_idx"] + 1) <= (len(responses) - 1):
            if do_reverse:
                responses.reverse()

            if shuffle:
                # https://stackoverflow.com/a/19307329/18121288
                random.Random(shuffle_seed).shuffle(responses)

            response_config["last_response_idx"] += 1
            response = responses[response_config["last_response_idx"]]
            dprint(response) if enable_dprint else print(response)

        return response_config

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
                    # self.func_dict[skillname]()
                    pass

            elif exec_engine == "AOs":
                pass

            elif exec_engine == "skills":
                pass
 