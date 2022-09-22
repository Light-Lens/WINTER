from Core import *

Command = sys.argv[1]

Speak(WINTER.add_sir(WINTER.assure()))
Weather, City = WeatherReport()

# T1, T2: Template
T1 = [["Today's weather", "The weather"], ["outsite", f"in {City}"], [f"is {Weather}."]]
T2 = [[f"It will be a {Weather} day"], ["outside.", f"in {City}."]]

# S1, S2: Sentence
S1 = ArrangeWords(T1)
S2 = ArrangeWords(T2)

out = numpy.random.choice([S1, S2])
out = WINTER.add_sir(out)
Speak(out.capitalize())
