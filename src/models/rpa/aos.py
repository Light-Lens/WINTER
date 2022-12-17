from src.models.lang.alphabet import Classify
from src.utils import ArrangeWords
import re

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

class aos:
    def __init__(self):
        self.output = ""
        self.list_of_outputs = []

        self.Classifier = Classify("models\\intents.json", "models\\and.pth", "and")
        self.Classifier.init()

    def formatter(self, text, tokens=[]):
        if not tokens: tokens = lexer(text).tokenizer()
        text_split = text.split(" and ")
        list_of_commands = [[]]

        count = 1
        for i in tokens:
            if i == "and":
                prev_text, next_text = text_split[count-1], text_split[count]
                tag = self.Classifier.predict(f"{prev_text} and {next_text}")

                if tag == "true": list_of_commands.append([])
                else: list_of_commands[-1].append(i)

                count += 1

            else: list_of_commands[-1].append(i)
        return list_of_commands

    def interpreter(self, cmd="default", args=[]):
        pass
