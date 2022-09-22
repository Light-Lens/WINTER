from Core import *

Command = sys.argv[1]

Speak(WINTER.add_sir(WINTER.assure()))
ans, question = CalcMath(Command)

# T1, T2: Template
T1 = [[question], ["is", "="], [ans], ["."]]

# S1, S2: Sentence
S1 = ArrangeWords(T1)

out = WINTER.add_sir(S1)
Speak(out.capitalize())
