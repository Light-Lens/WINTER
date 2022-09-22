from Core import *

Command = sys.argv[1]

Speak(WINTER.add_sir(WINTER.assure()))
Time = GetTime()

# T1, T2: Template
T1 = [["It's", "It is"], [Time], [f"in the {GreetUs()}", f"in {GreetUs()}", 9]]

# S1, S2: Sentence
S1 = ArrangeWords(T1)

out = WINTER.add_sir(S1)
Speak(out.capitalize())
