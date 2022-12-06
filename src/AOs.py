from src.alphabet import Classify
from src.components import *
import sys, re

Classifier = Classify("models\\and.json", "models\\and.pth")
Classifier.initalize()

class lexer:
    def __init__(self, line:str):
        self.line = line

    def tokenizer(self):
        tokens = re.findall(r'\".*\"|[\d\s+\.\+\-\*\/\(\)]+|[^\s,?]+', self.line)

        # remove empty-space from tokens
        tokens = [s.strip('"') for s in tokens]
        tokens = [s.strip() for s in tokens]

        # remove empty strings
        return list(filter(None, tokens))

class AOs:
    def __init__(self):
        self.output = ""
        self.list_of_outputs = []

    @staticmethod
    def formatter(text, tokens=[]):
        if not tokens: tokens = lexer(text).tokenizer()
        text_split = text.split(" and ")
        list_of_commands = [[]]

        count = 1
        for i in tokens:
            if i == "and":
                prev_text, next_text = text_split[count-1], text_split[count]
                tag, _ = Classifier.get_response(f"{prev_text} and {next_text}")

                if tag == "true": list_of_commands.append([])
                else: list_of_commands[-1].append(i)

                count += 1

            else: list_of_commands[-1].append(i)
        return list_of_commands

    def interpreter(self, cmd="default", args=[""]):
        for i in args:
            if cmd == "default": self.output = Chat(i)
            elif cmd == "bye": sys.exit()
            elif cmd == "lock pc": self.output = LockPC()
            elif cmd == "restart pc": self.output = RestartPC()
            elif cmd == "shutdown pc": self.output = ShutdownPC()
            # elif cmd == "train": self.output = SelfTrain()

            elif cmd == "mute": self.output = MutePC()
            elif cmd == "time": self.output = GetTime()
            elif cmd == "date": self.output = GetDate()
            elif cmd == "greet": self.output = GreetUs()
            elif cmd == "joke": self.output = CrackJokes()
            elif cmd == "fact": self.output = Facts()
            elif cmd == "weather": self.output = WeatherReport()
            elif cmd == "temperature": self.output = WeatherTemp()
            elif cmd == "resizewindow": self.output = MiniMaxTask()

            elif cmd == "start": self.output = OpenSitesOrApps(i)
            elif cmd == "play pc": self.output = PlayOfflineMedia(i)
            elif cmd == "close app": self.output = KillTask(i)
            elif cmd == "switch": self.output = SwitchTask(i)
            elif cmd == "project": self.output = CreateProject(i)
            elif cmd == "play youtube": self.output = PlayOnYT(i)

            elif cmd == "math": self.output = CalcMath(i)
            elif cmd == "search": self.output = SearchOnline(i)
            elif cmd == "summarize": self.output = Summarize(i)
            elif cmd == "translate": self.output = Translate(i)
            else: self.output = ""
            self.list_of_outputs.append(self.output)
