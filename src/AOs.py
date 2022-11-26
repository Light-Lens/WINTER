from src import components
import sys, re

class lexer:
    def __init__(self, line:str):
        self.line = line

    def tokenizer(self):
        tokens = re.findall(r'\".*\"|[-+]?\d[-+*\.\/x]\d|\w+', self.line)

        # remove empty-space from tokens
        tokens = [s.strip('"') for s in tokens]
        tokens = [s.strip() for s in tokens]

        # remove empty strings
        return list(filter(None, tokens))

class AOs:
    def __init__(self):
        self.input = ""
        self.output = []

    def clear(self):
        self.input = ""
        self.output = []

    def formatter(self):
        tokens = lexer(self.input).tokenizer()
        list_of_commands = [[]]

        for i in tokens:
            if i == "and": list_of_commands.append([])
            else: list_of_commands[-1].append(i)

        return list_of_commands

    def interpreter(self, tokens):
        args = tokens[1:] if len(tokens) > 0 else []
        cmd = tokens[0]

        if cmd == "exit": sys.exit()
        elif cmd == "lock": components.LockPC()
        elif cmd == "restart": components.RestartPC()
        elif cmd == "shutdown": components.ShutdownPC()

        elif cmd == "time": self.output.append( components.GetTime() )
        elif cmd == "date": self.output.append( components.GetDate() )
        elif cmd == "greet": self.output.append( components.GreetUs() )
        elif cmd == "temp": self.output.append( components.WeatherTemp() )
        elif cmd == "joke": self.output.append( components.CrackJokes() )
        elif cmd == "fact": self.output.append( components.Facts() )
        elif cmd == "weather": self.output.append( components.WeatherReport() )

        elif cmd == "open" and args: components.OpenSitesOrApps(args[0])
        elif cmd == "play" and args: components.PlayOfflineMedia(args[0])
        elif cmd == "close" and args: components.KillTask(args[0])
        elif cmd == "switch" and args: components.SwitchTask(args[0])
        elif cmd == "create" and args: components.CreateProject(args[0])
        elif cmd == "youtube" and args: components.PlayOnYT(args[0])
        elif cmd == "resizewindow" and args: components.MiniMaxTask()

        elif cmd == "calc" and args: self.output.append( components.CalcMath(args[0]) )
        elif cmd == "search" and args: self.output.append( components.SearchOnline(args) )
        elif cmd == "summary" and args: self.output.append( components.Summarize(args[0]) )
        elif cmd == "translate" and args: self.output.append( components.Translate(args[0]) )
        else: self.output.append("")
