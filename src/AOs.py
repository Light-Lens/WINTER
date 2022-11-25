import components
import re

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
        self.list_of_commands = [[]]

    def clear(self):
        self.input = ""
        self.output = []
        self.list_of_commands = [[]]

    def formatter(self):
        tokens = lexer(self.input).tokenizer()

        count = 0
        for i in tokens:
            if i == "and":
                count += 1
                self.list_of_commands.append([])

            else: self.list_of_commands[count].append(i)
        return self.list_of_commands

    def interpreter(self):
        tokens = self.formatter()
        for i, e in enumerate(tokens):
            cmd = e[0]
            args = e[1:] if len(tokens) > 0 else []

            if cmd == "lock": components.LockPC()
            elif cmd == "restart": components.RestartPC()
            elif cmd == "shutdown": components.ShutdownPC()

            elif cmd == "time": self.output.append( components.GetTime() )
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

a = AOs()
a.input = ''
a.interpreter()
# print(a.output)
