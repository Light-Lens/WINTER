from src.components import *
import sys, re

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
        self.input = ""
        self.output = ""
        self.list_of_outputs = []

    def formatter(self):
        tokens = lexer(self.input).tokenizer()
        list_of_commands = [[]]

        for i in tokens:
            if i == "and": list_of_commands.append([])
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
        elif cmd == "resizewindow": self.output = MiniMaxTask()

        elif cmd == "time": self.output = GetTime()
        elif cmd == "date": self.output = GetDate()
        elif cmd == "greet": self.output = GreetUs()
        elif cmd == "temp": self.output = WeatherTemp()
        elif cmd == "joke": self.output = CrackJokes()
        elif cmd == "fact": self.output = Facts()
        elif cmd == "weather": self.output = WeatherReport()

        elif cmd == "open" and args: self.output = OpenSitesOrApps(args[0])
        elif cmd == "play" and args: self.output = PlayOfflineMedia(args[0])
        elif cmd == "close" and args: self.output = KillTask(args[0])
        elif cmd == "switch" and args: self.output = SwitchTask(args[0])
        elif cmd == "create" and args: self.output = CreateProject(args[0])
        elif cmd == "youtube" and args: self.output = PlayOnYT(args[0])

        elif cmd == "chat" and args: self.output = Chat(args[0])
        elif cmd == "calc" and args: self.output = CalcMath(args[0])
        elif cmd == "search" and args: self.output = SearchOnline(args)
        elif cmd == "summary" and args: self.output = Summarize(args[0])
        elif cmd == "translate" and args: self.output = Translate(args[0])
        else: self.output = ""
        self.list_of_outputs.append(self.output)
