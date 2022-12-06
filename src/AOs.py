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

    def interpreter(self, tokens):
        if not tokens: return None
        args = tokens[1:] if len(tokens) > 0 else []
        cmd = tokens[0]

        if cmd == "exit": sys.exit()
        elif cmd == "lock": self.output = LockPC()
        elif cmd == "restart": self.output = RestartPC()
        elif cmd == "shutdown": self.output = ShutdownPC()
        elif cmd == "train": self.output = SelfTrain()

        elif cmd == "mute": self.output = MutePC()
        elif cmd == "time": self.output = GetTime()
        elif cmd == "date": self.output = GetDate()
        elif cmd == "greet": self.output = GreetUs()
        elif cmd == "temp": self.output = WeatherTemp()
        elif cmd == "joke": self.output = CrackJokes()
        elif cmd == "fact": self.output = Facts()
        elif cmd == "weather": self.output = WeatherReport()
        elif cmd == "resizewindow": self.output = MiniMaxTask()

        elif cmd == "open" and args: self.output = OpenSitesOrApps(args[0])
        elif cmd == "play" and args: self.output = PlayOfflineMedia(args[0])
        elif cmd == "close" and args: self.output = KillTask(args[0])
        elif cmd == "switch" and args: self.output = SwitchTask(args[0])
        elif cmd == "create" and args: self.output = CreateProject(args[0])
        elif cmd == "youtube" and args: self.output = PlayOnYT(args[0])

        elif cmd == "calc" and args: self.output = CalcMath(args[0])
        elif cmd == "search" and args: self.output = SearchOnline(args)
        elif cmd == "summary" and args: self.output = Summarize(args[0])
        elif cmd == "translate" and args: self.output = Translate(args[0])
        else: self.output = ""
        self.list_of_outputs.append(self.output)
