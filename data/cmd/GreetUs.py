from Core import *

Command = sys.argv[1]

Speak(WINTER.add_sir(WINTER.assure()))
TimeOfTheDay = GreetUs()

# T1, T2: Template
T1 = [["Good"], [TimeOfTheDay], [".", ",", 3]]
T2 = [["Hope you have a good day.", "Hope you enjoy your day.", 8]]
T3 = [["Hope you are having a good day.", "Hope you are enjoying your day."]]
T4 = [["Hope you had a good day.", "Hope you enjoyed your day."]]
T5 = [[f"It's {TimeOfTheDay} already.", 4], ["You should now probably sleep.", "You should probably sleep now."]]

# S1, S2: Sentence
S1 = ArrangeWords(T1)
S2 = ArrangeWords(T2)
S3 = ArrangeWords(T3)
S4 = ArrangeWords(T4)
S5 = ArrangeWords(T5)

if TimeOfTheDay == "Morning":
    # TODO: Make sure it will only greet this way once.
    out = " ".join([S1, S2])
    out = WINTER.add_sir(out)
    Speak(out.capitalize())

    WeatherDialogues = [1, 2, 3]
    WeatherDialogues.extend([0]*8)
    MorningReport = numpy.random.choice(WeatherDialogues)
    if MorningReport == 1: import WeatherReport
    elif MorningReport == 2: import TempReport
    elif MorningReport == 3: import TempReport, WeatherReport

elif TimeOfTheDay == "Afternoon":
    out = " ".join([S1, S3])
    out = WINTER.add_sir(out)
    Speak(out.capitalize())

elif TimeOfTheDay == "Evening":
    out = " ".join([S1, S4])
    out = WINTER.add_sir(out)
    Speak(out.capitalize())

elif TimeOfTheDay == "Night":
    out = " ".join([S1, S5])
    out = WINTER.add_sir(out)
    Speak(out.capitalize())
