import win32process, webbrowser, wikipedia, randfacts, pywhatkit, pyautogui, requests, datetime, pyjokes
import psutil, heapq, numpy, re, os

from nltk_utils import tokenize, sent_tokenize
from googletrans import Translator
from alphabet import ClassifyIntent
from nltk.corpus import stopwords

# init modules
translator = Translator()

# TODO: (\d.*\d) is the regex expression to fetch math expression from a string

# Do math
# https://medium.com/codex/another-python-question-that-took-me-days-to-solve-as-a-beginner-37b5e144ecc
def CalcMath(Query):
    expression = Query.replace(" ", "")
    regex = re.findall(r'(\d.*\d)', Query)
    if not regex: return None

    expression = regex[0]

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

    lis = splitby(expression, "+-")
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

    
    for i in range(len(lis)): lis[i] = evaluate_mul_div(lis[i])
    output = float(lis[0])
    lis = lis[1:]

    while len(lis) > 0:
        operator = lis[0]
        number = float(lis[1])
        lis = lis[2:]

        if operator == "+": output += number
        elif operator == "-": output -= number

    return output

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

    return {"City": City, "Weather": res.text}

# Get today's temperature.
def WeatherTemp(City="Bhagalpur"):
    # https://medium.com/analytics-vidhya/forecast-weather-using-python-e6f5519dc3c1
    print(F"Displaying temperature in: {City}")

    # Fetch weather details.
    URL = f"https://wttr.in/{City}?format=%t"
    res = requests.get(URL)
    Temp = res.text[1:] if res.text[0] == "+" else res.text

    return {"City": City, "Temperature": Temp}

# Translate to any language
def Translate(Query):
    #TODO: For now it only translates only to english, change it in future.
    regex = re.findall(r'translate this to english (.*)|translate to english (.*)|translate this (.*)|translate (.*)', Query)
    if regex:
        regex = [j for i in regex for j in list(filter(None, i))]
        Query = str(" ".join(i for i in regex)).strip()

    out = translator.translate(Query, dest="en")
    return {"Sentence": Query, "Translation": out.text, "Source": out.src}

# Search and play media on YouTube.
def PlayOnYT(Query):
    regex = re.findall(r'play from yt (.*)|search from yt (.*)|search from youtube (.*)|play from youtube (.*)|play on yt (.*)|search on yt (.*)|search on youtube (.*)|play on youtube (.*)|play (.*)', Query)
    if regex:
        regex = [j for i in regex for j in list(filter(None, i))]
        Query = str(" ".join(i for i in regex)).strip()

    video_link = pywhatkit.playonyt(Query)
    return {"Search query": Query, "Link": video_link}

# Get the current time
def GetTime():
    Hrs = int(datetime.datetime.now().hour)
    Mins = int(datetime.datetime.now().minute)
    Secs = int(datetime.datetime.now().second)
    CTime = f"{Hrs-12}:{Mins} PM" if Hrs >= 13 else f"{Hrs}:{Mins} AM"
    return {"Time": CTime, "Hour": Hrs, "Minutes": Mins, "Seconds": Secs}

# Create a new project
def CreateProject(Query):
    regex = re.findall(r'([create|make|start]* a (.*) (indexed|index it|marked|mark it|named|name it)[ as ]*(.*))|[create|make|start]* a (.*)', Query)
    if regex:
        regex = [j for i in regex for j in list(filter(None, i))]
        if not any(i in regex for i in ["indexed", "index it", "marked", "mark it", "named", "name it"]):
            return "No project name"

        proj_name = str(regex[2]).capitalize()
        location = f"D:\\Dev Projects\\{proj_name}"

        os.mkdir(location)
        return {"Project name": proj_name, "Project dir": location}
    return False

# Tell some joke
def CrackJokes():
    return pyjokes.get_joke(language="en", category="all")

# Tell some facts
def Facts():
    return randfacts.get_fact()

# Summarize any text
def Summarize(Query):
    regex = re.findall(r'summary on (.*)|summarize (.*)|summary of (.*)|(.*) summarize it|summary (.*)', Query)
    if regex:
        regex = [j for i in regex for j in list(filter(None, i))]
        Query = str(" ".join(i for i in regex)).strip()

    # First try searching on Wikipedia.
    try:
        article_text = wikipedia.summary(Query, sentences=5)

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

        return {"Query": Query, "Summary": summary}
    except Exception as e: return False

# Search on Google or Wikipedia.
def SearchOnline(Query):
    regex = re.findall(r'.* wikipedia for (.*)|.* google for (.*)|search on wikipedia (.*)|search on google (.*)|search for (.*)|search on (.*)|search (.*)', Query)
    if regex:
        regex = [j for i in regex for j in list(filter(None, i))]
        Query = str(" ".join(i for i in regex)).strip()

    # First try searching on Wikipedia.
    try:
        site_link = pywhatkit.search(Query)
        Results = wikipedia.summary(Query, sentences=2)

    # If error caught then search on Google.
    except Exception as e: Results = ""
    return {"Query": Query, "Site link": site_link, "Info": Results}

# Play offline media
def PlayOfflineMedia(Query):
    # List all the files in the given directory and play them randomly.
    def StartPlaying(Directory):
        Files = os.listdir(Directory)
        Media = os.path.join(Directory, numpy.random.choice(Files))
        os.startfile(Media)
        return Media

    media = {}
    media["pic"] = ClassifyIntent(Query, ["show a picture", "show a pic", "open any pic", "open me some picture", "show a photo", "open any image", "open me some image", "can you please show a photo"])
    media["song"] = ClassifyIntent(Query, ["play a song", "hit me with some music", "hit any music" "hit some music", "play me some music", "can you please play a song"])
    media["video"] = ClassifyIntent(Query, ["play a video", "play any video", "play me some video", "can you please play a video"])
    media_with_highest_confidence = max(media, key=media.get)

    if media_with_highest_confidence == "song":
        Dir = "D:\\Srijan\\Music"
        Name = StartPlaying(Dir)

    elif media_with_highest_confidence == "video":
        Dir = "D:\\Srijan\\Videos"
        Name = StartPlaying(Dir)

    elif media_with_highest_confidence == "pic":
        Dir = "D:\\Srijan\\Pictures"
        Name = StartPlaying(Dir)

    else: return False
    return {"Name": Name, "Location": Dir}

# Close an app.
def KillTask(Query):
    regex = re.findall(r'.* this app| .* current app|exit (\w+)|kill (\w+)|close (\w+)|quit (\w+)|shutdown (\w+)', Query)
    Apps = [j for i in regex for j in list(filter(None, i))] if regex else []

    if Apps:
        for i in Apps:
            for process in psutil.process_iter():
                process_name = process.name()
                if i in process_name.lower(): os.system(f"taskkill /f /im {process_name}")

    else:
        # https://stackoverflow.com/a/70574370/18121288
        hwnd = pyautogui.getActiveWindow()._hWnd
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        os.system(f"taskkill /f /im {process_name}")

    return {"Closed app": process_name}

# Switch window
def SwitchWindows(Query):
    tasks = list(filter(None, pyautogui.getAllTitles()))
    tasks.remove("Microsoft Text Input Application")
    tasks.remove("Program Manager")

    regex = re.findall(r'switch to (.*)|switch (.*)|change to (.*)|change (.*)', Query)
    Apps = [j for i in regex for j in list(filter(None, i))] if regex else []

    if "window" in Apps or "app" in Apps:
        CurrentTask = pyautogui.getActiveWindowTitle()
        if CurrentTask.lower() in [i.lower() for i in tasks]:
            title = tasks[tasks.index(CurrentTask) + 1]

            pyautogui.keyDown('alt')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('alt')

    else:
        app_score = [[ClassifyIntent(Apps[0], [i]), i] for i in tasks]
        title = sorted(app_score, reverse=True)[0][1]
        idx = tasks.index(title)

        pyautogui.keyDown('alt')
        for _ in range(idx): pyautogui.press('tab')

        pyautogui.keyUp('alt')

# Open Sites or Apps
def OpenSitesOrApps(Query):
    def OpenExtentionFunc(Keyword, Link, OpenWith):
        if Keyword in Query:
            if OpenWith == "search": pywhatkit.search(Link)
            elif OpenWith == "browser": webbrowser.open(Link)
            elif OpenWith == "system": os.startfile(Link)

    # News and Temperature news
    OpenExtentionFunc("news", "news", "search")
    OpenExtentionFunc("weather", "weather", "search")
    OpenExtentionFunc("temperature", "temperature", "search")

    # Open websites
    OpenExtentionFunc("google", "www.google.com", "browser")
    OpenExtentionFunc("yt", "www.youtube.com", "browser")
    OpenExtentionFunc("youtube", "www.youtube.com", "browser")
    OpenExtentionFunc("insta", "www.instagram.com/?theme=dark", "browser")
    OpenExtentionFunc("instagram", "www.instagram.com/?theme=dark", "browser")
    OpenExtentionFunc("facebook", "www.facebook.com", "browser")
    OpenExtentionFunc("twitter", "twitter.com", "browser")
    OpenExtentionFunc("whatsapp", "web.whatsapp.com", "browser")
    OpenExtentionFunc("github", "github.com", "browser")
    OpenExtentionFunc("scratch", "scratch.mit.edu", "browser")
    OpenExtentionFunc("studybyte", "light-lens.github.io/Studybyte", "browser")
    OpenExtentionFunc("chrome dino", "chrome://dino", "browser")

    # Open Apps
    OpenExtentionFunc("edge", "msedge", "system")
    OpenExtentionFunc("chrome", "chrome", "system")
    OpenExtentionFunc("firefox", "firefox", "system")
    OpenExtentionFunc("windows termianl", "wt", "system")
    OpenExtentionFunc("cmd", "cmd", "system")
    OpenExtentionFunc("command prompt", "cmd", "system")
    OpenExtentionFunc("calculator", "ms-calculator:", "system")
    OpenExtentionFunc("clock", "ms-clock:", "system")
    OpenExtentionFunc("camera", "microsoft.windows.camera:", "system")
    OpenExtentionFunc("music", "mswindowsmusic:", "system")
    OpenExtentionFunc("mail", "outlookmail:", "system")
    OpenExtentionFunc("microsoft store", "ms-windows-store:", "system")
    OpenExtentionFunc("windows security", "windowsdefender:", "system")
    OpenExtentionFunc("onenote", "onenote:", "system")
    OpenExtentionFunc("onedrive", os.getenv("onedrive"), "system")
    OpenExtentionFunc("paint", "mspaint", "system")
    OpenExtentionFunc("notepad", "notepad", "system")
    OpenExtentionFunc("code", "code", "system")
    OpenExtentionFunc("paint 3d", "ms-paint:", "system")
    OpenExtentionFunc("photos", "ms-photos:", "system")
    OpenExtentionFunc("screen snip", "ms-screenclip:", "system")
    OpenExtentionFunc("settings", "ms-settings:", "system")
    OpenExtentionFunc("snip and sketch", "ms-ScreenSketch:", "system")
    OpenExtentionFunc("minecraft", "minecraft:", "system")
    OpenExtentionFunc("candy crush", "candycrushsodasaga:", "system")
