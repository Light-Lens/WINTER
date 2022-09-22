from Core import *

Command = sys.argv[1]

Speak(WINTER.add_sir(WINTER.assure()))
Temp, City = WeatherTemp()

# T1, T2: Template
T1 = [["Today's", "The"], ["temperature", "weather"], ["outsite", f"in {City}"], [f"is {Temp}."]]

# S1, S2: Sentence
S1 = ArrangeWords(T1)

out = WINTER.add_sir(S1)
Speak(out.capitalize())
