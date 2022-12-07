from src.alphabet import Classify
from src.nltk_utils import ArrangeWords
from src.skills import *
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

    def interpreter(self, cmd="default", args=[""], responses: list=None):
        for i in args:
            if cmd == "default" or cmd == "chat": self.output = Chat(i)
            elif cmd == "bye":
                daytime = GreetUs()

                greeting = []
                if daytime == "Morning": greeting.append(ArrangeWords(responses[0]))
                elif daytime == "Afternoon": greeting.append(ArrangeWords(responses[1]))
                elif daytime == "Evening": greeting.append(ArrangeWords(responses[2]))
                elif daytime == "Night": greeting.append(ArrangeWords(responses[3]))

                Speak("\n".join(greeting))
                sys.exit()

            elif cmd == "lock pc": LockPC()
            elif cmd == "restart pc": RestartPC()
            elif cmd == "shutdown pc": ShutdownPC()
            elif cmd == "train": SelfTrain()

            elif cmd == "mute": MutePC()
            elif cmd == "time":
                time = GetTime()
                self.output = ArrangeWords(responses).replace("<1>", time)

            elif cmd == "date":
                date = GetDate()
                self.output = ArrangeWords(responses).replace("<1>", date)

            elif cmd == "greet":
                daytime = GreetUs()
                greetday = ArrangeWords(responses[0])

                greeting = []
                greeting.append(greetday.replace("<1>", daytime))
                if daytime == "Morning": greeting.append(ArrangeWords(responses[1:][0]))
                elif daytime == "Afternoon": greeting.append(ArrangeWords(responses[1:][1]))
                elif daytime == "Evening": greeting.append(ArrangeWords(responses[1:][2]))
                elif daytime == "Night": greeting.append(ArrangeWords(responses[1:][3]))

                self.output = "\n".join(greeting)

            elif cmd == "joke": self.output = CrackJokes()
            elif cmd == "fact": self.output = Facts()
            elif cmd == "weather":
                weather, city = WeatherReport()
                response = ArrangeWords(responses)
                self.output = response.replace("<1>", city).replace("<2>", weather)

            elif cmd == "temperature":
                temp, city = WeatherTemp()
                response = ArrangeWords(responses)
                self.output = response.replace("<1>", city).replace("<2>", temp)

            elif cmd == "resizewindow": MiniMaxTask()
            elif cmd == "start":
                self.output = ArrangeWords(responses)
                OpenSitesOrApps(i)

            elif cmd == "play pc":
                self.output = ArrangeWords(responses)
                PlayOfflineMedia(i)

            elif cmd == "close app":
                appname = KillTask(i)
                self.output = ArrangeWords(responses).replace("<1>", appname)

            elif cmd == "switch":
                self.output = ArrangeWords(responses)
                SwitchTask(i)

            elif cmd == "project":
                proj_name = CreateProject(i)
                self.output = ArrangeWords(responses).replace("<1>", proj_name)

            elif cmd == "play youtube":
                self.output = ArrangeWords(responses)
                PlayOnYT(i)

            elif cmd == "math":
                expr, result = CalcMath(i)
                response = ArrangeWords(responses)
                self.output = response.replace("<1>", expr).replace("<2>", result)

            elif cmd == "search":
                search = SearchOnline(i)
                response = ArrangeWords(responses)
                self.output = "\n".join([response, search])

            elif cmd == "summarize":
                summary = Summarize(i)

                response = ArrangeWords(responses)
                self.output = "\n".join([response, summary])

            elif cmd == "translate": self.output = Translate(i)
            else: self.output = ""
            self.list_of_outputs.append(self.output)
