from Core import *

Command = sys.argv[1]

Speak(WINTER.add_sir(WINTER.assure()))
fails_count = 0

while CreateProject(Command) == "No project name":
    T1 = [["What"], ["shall", "may", "should"], ["I"], ["name", "call", "save", "index", "mark"] ["it"], ["as", 3], ["?"]]
    out = WINTER.add_sir(ArrangeWords(T1))
    Speak(out.capitalize())

    Command = TakeCommand()
    Command = f"Create a new project and named it as {Command}"
    fails_count += 1

T2 = [["Initializing project,", "Initialized project,", "Creating project,", "Started project,", "Starting project,"],
    ["Shall", "Can"], ["we"], ["start"], ["?"]]

out = WINTER.add_sir(ArrangeWords(T2))
Speak(out.capitalize())
