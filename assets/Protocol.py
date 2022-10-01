from assets.components import *
from assets.core import *

def assure():
    Speak(w2.add_sir(w2.assure())) if random.randrange(11) > 7 else None

class Protocol:
    def CalcMath(Command):
        assure()
        ans, question = CalcMath(Command)

        # T1, T2: Template
        T1 = [[question], ["is", "="], [ans]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)
        Speak(S1)

    def CrackJokes():
        assure()
        Speak(CrackJokes())

    def CreateProject(Command):
        assure()

        while CreateProject(Command) == "No project name" or not CreateProject(Command):
            T1 = [["What"], ["shall", "may", "should"], ["I"], ["name", "call", "save", "index", "mark"], ["it"], ["as", 3]]
            out = w2.add_sir(ArrangeWords(T1) + "?")
            Speak(out)

            Projname = TakeCommand()
            Command = f"start a new project marked as {Projname}"

        T2 = [["Initializing project,", "Initialized project,", "Creating project,", "Started project,", "Starting project,"],
            ["Shall", "Can"], ["we"], ["start"]]

        out = w2.add_sir(ArrangeWords(T2) + "?")
        Speak(out.capitalize())

    def Exit():
        assure()
        sys.exit()

    def Summarize(Command):
        assure()
        Speak(Summarize(Command))

    def Facts():
        assure()
        Speak(Facts())

    def GetTime():
        assure()
        Time, _ = GetTime()

        # T1, T2: Template
        T1 = [["It's", "It is"], [Time], [f"in the {GreetUs()}", f"in {GreetUs()}", 9]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)

        out = w2.add_sir(S1)
        Speak(out.capitalize())

    def GreetUs():
        assure()
        TimeOfTheDay = GreetUs()
        _, Hour = GetTime()

        # T1, T2: Template
        T1 = [["Good"], [f"{TimeOfTheDay}.", f"{TimeOfTheDay},"]]
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
            out = w2.add_sir(out)
            Speak(out.capitalize())

            if Hour[0] >= 4 and Hour[0] <= 7:
                WeatherDialogues = [1, 2, 3]
                WeatherDialogues.extend([0]*8)
                MorningReport = numpy.random.choice(WeatherDialogues)

                if MorningReport == 1: Protocol.WeatherReport()
                elif MorningReport == 2: Protocol.TempReport()
                elif MorningReport == 3:
                    Protocol.TempReport()
                    Protocol.WeatherReport()

        elif TimeOfTheDay == "Afternoon":
            out = " ".join([S1, S3])
            out = w2.add_sir(out)
            Speak(out.capitalize())

        elif TimeOfTheDay == "Evening":
            out = " ".join([S1, S4])
            out = w2.add_sir(out)
            Speak(out.capitalize())

        elif TimeOfTheDay == "Night":
            out = " ".join([S1, S5])
            out = w2.add_sir(out)
            Speak(out.capitalize())

    def KillTask(Command):
        assure()
        KillTask(Command)

    def LockPC():
        assure()
        LockPC()

    def OpenSitesOrApps(Command):
        assure()
        OpenSitesOrApps(Command)

    def PlayOfflineMedia(Command):
        assure()
        PlayOfflineMedia(Command)

    def PlayOnYT(Command):
        assure()
        PlayOnYT(Command)

    def RestartPC():
        assure()
        RestartPC()

    def SearchOnline(Command):
        assure()
        Speak(SearchOnline(Command))

    def ShutdownPC():
        assure()
        ShutdownPC()

    def SwitchWindows(Command):
        assure()
        SwitchWindows(Command)

    def TempReport():
        assure()
        Temp, City = WeatherTemp()

        # T1, T2: Template
        T1 = [["Today's", "The"], ["temperature", "weather"], ["outsite", f"in {City}"], [f"is {Temp}."]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)

        out = w2.add_sir(S1)
        Speak(out.capitalize())

    def Translate(Command):
        assure()
        Speak(Translate(Command))

    def WeatherReport():
        assure()
        Weather, City = WeatherReport()

        # T1, T2: Template
        T1 = [["Today's weather", "The weather"], ["outsite", f"in {City}"], [f"is {Weather}."]]
        T2 = [[f"It will be a {Weather} day"], ["outside.", f"in {City}."]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)
        S2 = ArrangeWords(T2)

        out = numpy.random.choice([S1, S2])
        out = w2.add_sir(out)
        Speak(out.capitalize())
