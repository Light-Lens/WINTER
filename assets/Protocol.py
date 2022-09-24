from assets.components import *
from assets.core import *

class Protocol:
    def CalcMath(Command):
        Speak(w2.add_sir(w2.assure()))
        ans, question = CalcMath(Command)

        # T1, T2: Template
        T1 = [[question], ["is", "="], [ans], ["."]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)

        out = w2.add_sir(S1)
        Speak(out.capitalize())

    def CrackJokes():
        Speak(w2.add_sir(w2.assure()))
        Speak(CrackJokes())

    def CreateProject(Command):
        Speak(w2.add_sir(w2.assure()))

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
        Speak(w2.add_sir(w2.assure()))
        sys.exit()

    def Facts():
        Speak(w2.add_sir(w2.assure()))
        Speak(Facts())

    def GetTime():
        Speak(w2.add_sir(w2.assure()))
        Time, _ = GetTime()

        # T1, T2: Template
        T1 = [["It's", "It is"], [Time], [f"in the {GreetUs()}", f"in {GreetUs()}", 9]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)

        out = w2.add_sir(S1)
        Speak(out.capitalize())

    def GreetUs():
        Speak(w2.add_sir(w2.assure()))
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
        Speak(w2.add_sir(w2.assure()))
        KillTask(Command)

    def LockPC():
        Speak(w2.add_sir(w2.assure()))
        LockPC()

    def OpenSitesOrApps(Command):
        Speak(w2.add_sir(w2.assure()))
        OpenSitesOrApps(Command)

    def PlayOfflineMedia(Command):
        Speak(w2.add_sir(w2.assure()))
        PlayOfflineMedia(Command)

    def PlayOnYT(Command):
        Speak(w2.add_sir(w2.assure()))
        PlayOnYT(Command)

    def RestartPC():
        Speak(w2.add_sir(w2.assure()))
        RestartPC()

    def SearchOnline(Command):
        Speak(w2.add_sir(w2.assure()))
        Speak(SearchOnline(Command))

    def ShutdownPC():
        Speak(w2.add_sir(w2.assure()))
        ShutdownPC()

    def SwitchWindows(Command):
        Speak(w2.add_sir(w2.assure()))
        SwitchWindows(Command)

    def TempReport():
        Speak(w2.add_sir(w2.assure()))
        Temp, City = WeatherTemp()

        # T1, T2: Template
        T1 = [["Today's", "The"], ["temperature", "weather"], ["outsite", f"in {City}"], [f"is {Temp}."]]

        # S1, S2: Sentence
        S1 = ArrangeWords(T1)

        out = w2.add_sir(S1)
        Speak(out.capitalize())

    def Translate(Command):
        Speak(w2.add_sir(w2.assure()))
        Speak(Translate(Command))

    def WeatherReport():
        Speak(w2.add_sir(w2.assure()))
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
