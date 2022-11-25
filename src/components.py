import win32process, webbrowser, subprocess, wikipedia, randfacts, pywhatkit, pyautogui, requests, datetime, pyjokes
import psutil, ctypes, heapq, numpy, re, os

from src.nltk_utils import tokenize, sent_tokenize, ClassifyIntent
from googletrans import Translator
from nltk.corpus import stopwords

# init modules
translator = Translator()

# This function has the same result as pressing Ctrl+Alt+Del and clicking Lock Workstation.
# https://stackoverflow.com/a/20733443/18121288
def LockPC():
    ctypes.windll.user32.LockWorkStation()

# shutdown /s -> shuts down the computer [but it takes time],
# also shows message windows is going to be shutdown within a minute,
# to avoid this we use /t parameter time = 0 seconds /t0, command = shutdown /s /t0, execute to the shell.
# https://stackoverflow.com/a/67342911/18121288
def ShutdownPC():
    os.system("shutdown /s /t0")

# shutdown /r -> restarts the computer [but it takes time],
# also shows message windows is going to be shutdown within a minute,
# to avoid this we use /t parameter time = 0 seconds /t0, command = shutdown /r /t0, execute to the shell.
# https://stackoverflow.com/a/67342911/18121288
def RestartPC():
    os.system("shutdown /r /t0")

# Minimize all apps
def MiniMaxTask():
    pyautogui.hotkey('super', 'd')

# Do math
# https://medium.com/codex/another-python-question-that-took-me-days-to-solve-as-a-beginner-37b5e144ecc
def CalcMath(expr):
    expr = expr.replace(" ", "")

    #* It can do "2 - 1" but fails to do "-1 + 2", solve it ~> (Solved)
    expr = expr if not expr.startswith("-") else "0" + expr

    def splitby(string, separators):
        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else: current += ch

        lis.append(current)
        return lis

    lis = splitby(expr, "+-")
    def evaluate_mul_div(string):
        lis = splitby(string, "x/")
        if len(lis) == 1: return lis[0]

        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "x": output *= number
            elif operator == "/": output /= number

        return output

    try:
        for i in range(len(lis)): lis[i] = evaluate_mul_div(lis[i])
        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "+": output += number
            elif operator == "-": output -= number

    except ZeroDivisionError: output = "undefined"

    output = output if not str(output).endswith(".0") else int(output)
    return f"{expr} = {output}"

# Greet the user according to the current time.
def GreetUs():
    time_of_the_day = ""
    Hour = int(datetime.datetime.now().hour)

    if Hour >= 0 and Hour < 12: time_of_the_day = "Morning"
    elif Hour >= 12 and Hour < 18: time_of_the_day = "Afternoon"
    elif Hour >= 18 and Hour < 22: time_of_the_day = "Evening"
    elif Hour >= 22 and Hour < 0: time_of_the_day = "Night"
    return time_of_the_day

# Get the weather report.
def WeatherReport(City="Bhagalpur"):
    # https://medium.com/analytics-vidhya/forecast-weather-using-python-e6f5519dc3c1
    print(f"Displaying weather report for: {City}")

    # Fetch weather details.
    URL = f"https://wttr.in/{City}?format=%C"
    res = requests.get(URL)

    return res.text, City

# Get today's temperature.
def WeatherTemp(City="Bhagalpur"):
    # https://medium.com/analytics-vidhya/forecast-weather-using-python-e6f5519dc3c1
    print(F"Displaying temperature in: {City}")

    # Fetch weather details.
    URL = f"https://wttr.in/{City}?format=%t"
    res = requests.get(URL)
    Temp = res.text[1:] if res.text[0] == "+" else res.text

    return Temp, City

# Translate to any language
def Translate(sent):
    out = translator.translate(sent, dest="en")
    return out.text

# Search and play media on YouTube.
def PlayOnYT(Query):
    video_link = pywhatkit.playonyt(Query)
    return video_link

# Get the current time
def GetTime():
    Hrs = int(datetime.datetime.now().hour)
    Mins = int(datetime.datetime.now().minute)
    CTime = f"{Hrs-12}:{Mins} PM" if Hrs >= 13 else f"{Hrs}:{Mins} AM"
    return CTime, [Hrs, Mins]

# # Create a new project
def CreateProject(proj_name="_git"):
    if proj_name == "_git": OpenSitesOrApps("new github project")
    else:
        dir = f"D:\\Dev Projects\\{proj_name}"

        if not os.path.exists(dir): os.mkdir(dir)
        return dir

# Tell some joke
def CrackJokes():
    return pyjokes.get_joke(language="en", category="all")

# Tell some facts
def Facts():
    return randfacts.get_fact()

# Summarize any text
def Summarize(Query):
    try:
        article_text = wikipedia.summary(Query.lower(), sentences=5)

        # Removing Square Brackets and Extra Spaces
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        # Removing special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

        sentence_list = sent_tokenize(article_text)
        stop_words = stopwords.words('english')

        word_frequencies = {}
        for word in tokenize(formatted_article_text):
            if word not in stop_words:
                if word not in word_frequencies.keys(): word_frequencies[word] = 1
                else: word_frequencies[word] += 1

        maximum_frequncy = max(word_frequencies.values())
        for word in word_frequencies.keys(): word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

        sentence_scores = {}
        for sent in sentence_list:
            for word in tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys(): sentence_scores[sent] = word_frequencies[word]
                        else: sentence_scores[sent] += word_frequencies[word]

        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)

        return summary
    except Exception as e: return ""

# Search on Google or Wikipedia.
def SearchOnline(Query):
    if Query[0] == "_search": pywhatkit.search(Query[1])
    else:
        try:
            pywhatkit.search(Query[0])
            return wikipedia.summary(Query[0], sentences=2)

        except Exception as e: pass
    return ""

# Play offline media
def PlayOfflineMedia(media):
    # List all the files in the given directory and play them randomly.
    def StartPlaying(Directory):
        Files = os.listdir(Directory)
        Media = os.path.join(Directory, numpy.random.choice(Files))
        os.startfile(Media)
        return Media

    if any(i in media for i in ["song", "music"]):
        Dir = "D:\\Srijan\\Music"
        Name = StartPlaying(Dir)

    elif any(i in media for i in ["video", "movie"]):
        Dir = "D:\\Srijan\\Videos"
        Name = StartPlaying(Dir)

    elif any(i in media for i in ["pic", "picture", "image", "photo"]):
        Dir = "D:\\Srijan\\Pictures"
        Name = StartPlaying(Dir)

    else: return False
    return Name

# Close an app.
def KillTask(appname):
    if appname == "_tab": pyautogui.hotkey('ctrl', 'w')
    elif appname == "_currentapp":
        # https://stackoverflow.com/a/70574370/18121288
        hwnd = pyautogui.getActiveWindow()._hWnd
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        os.system(f"taskkill /f /im {process_name}")
        return process_name

    else:
        hwnd = str(pyautogui.getWindowsWithTitle(appname)).replace("Win32Window(hWnd=", "")[1:-2]
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        os.system(f"taskkill /f /im {process_name}")
        return process_name

# Switch window
def SwitchTask(appname):
    if appname == "_tab": pyautogui.hotkey('ctrl', 'tab')
    elif appname == "_currentapp": pyautogui.hotkey('alt', 'tab')
    else:
        tasks = list(filter(None, pyautogui.getAllTitles()))
        tasks.remove("Microsoft Text Input Application")
        tasks.remove("Program Manager")

        app_score = ClassifyIntent(appname, tasks)
        title = app_score[1]
        idx = tasks.index(title)

        pyautogui.keyDown('alt')
        for _ in range(idx): pyautogui.press('tab')

        pyautogui.keyUp('alt')

# Open Sites or Apps
def OpenSitesOrApps(appname):
    proc = subprocess.Popen(["powershell", "get-StartApps", appname, "| Select-Object -ExpandProperty AppID"], stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()

    out = out.decode("utf-8")
    out = out.split("\r\n")
    out.pop()

    if out:
        AppID = out[0]
        os.system(f"start explorer shell:appsfolder\{AppID}")

    else: pywhatkit.search(appname)
