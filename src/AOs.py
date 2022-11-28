from src import components
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

    def clear(self):
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
        elif cmd == "lock": self.output = components.LockPC()
        elif cmd == "restart": self.output = components.RestartPC()
        elif cmd == "shutdown": self.output = components.ShutdownPC()
        elif cmd == "resizewindow": self.output = components.MiniMaxTask()

        elif cmd == "time": self.output = components.GetTime()
        elif cmd == "date": self.output = components.GetDate()
        elif cmd == "greet": self.output = components.GreetUs()
        elif cmd == "temp": self.output = components.WeatherTemp()
        elif cmd == "joke": self.output = components.CrackJokes()
        elif cmd == "fact": self.output = components.Facts()
        elif cmd == "weather": self.output = components.WeatherReport()

        elif cmd == "open" and args: self.output = components.OpenSitesOrApps(args[0])
        elif cmd == "play" and args: self.output = components.PlayOfflineMedia(args[0])
        elif cmd == "close" and args: self.output = components.KillTask(args[0])
        elif cmd == "switch" and args: self.output = components.SwitchTask(args[0])
        elif cmd == "create" and args: self.output = components.CreateProject(args[0])
        elif cmd == "youtube" and args: self.output = components.PlayOnYT(args[0])

        elif cmd == "chat" and args: self.output = components.Chat(args[0])
        elif cmd == "calc" and args: self.output = components.CalcMath(args[0])
        elif cmd == "search" and args: self.output = components.SearchOnline(args[0])
        elif cmd == "summary" and args: self.output = components.Summarize(args[0])
        elif cmd == "translate" and args: self.output = components.Translate(args[0])
        else: self.output = ""
        self.list_of_outputs.append(self.output)
