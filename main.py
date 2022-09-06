# WINTER
import speech_recognition as sr
import win32process
import webbrowser
import wikipedia
import randfacts
import pywhatkit
import pyautogui
import requests
import datetime
import pyjokes
import pyttsx3
import psutil
import random
import spacy
import heapq
import numpy
import json
import math
import sys
import re
import os

# Create multi-colored text in cmd.
from colorama import Fore, Style, init

# import google translate.
from googletrans import Translator, LANGUAGES

# operator module for keyword extractor
from operator import itemgetter

# NLTK modules
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Import 
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# init all modules if required
init(autoreset = True)
translator = Translator()
nlp = spacy.load('en_core_web_md')

# TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id) # Ivona's Brian voice
# engine.setProperty('voice', voices[0].id)

# PyTorch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

class Core:
    # Text to speech
    def Speak(audio):
        if audio:
            print(audio)
            engine.say(audio)
            engine.runAndWait()

    # Listen to the microphone and return a speech to text
    def TakeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print("> ", end="")
            audio = r.listen(source, phrase_time_limit=3)

        try:
            Query = r.recognize_google(audio, language = 'en-in')

            # Translate Hindi to English
            out = translator.translate(Query, dest="en")
            if LANGUAGES[out.src] != "english": Query = out.text

            print(Query)

        except Exception as e:
            print()
            return ""

        return Query

class alphabet():
    # Arrange words in such a way to form a logical sentence.
    def ArrangeWords(Words):
        # A number will represent the number of empty strings in a list.
        # For example: 4 -> ["", "", "", ""].
        for i in Words:
            for j in i:
                if isinstance(j, int):
                    EmptyList = [""] * j
                    i.extend(EmptyList)
                    i.remove(j)
                    break

        GreetingSentence = [numpy.random.choice(i) for i in Words]

        # Reconstruct the string to form a logical sentence.
        FinalSentence = " ".join(GreetingSentence)
        return FinalSentence

    # Calculate the cosine similarity
    def CalcCosine(sentence, pattern):
        def Lemmatizer(sentence):
            stop_words = set(stopwords.words("english"))
            tokens = nltk.tokenize.word_tokenize(sentence)
            Lemmatizer = WordNetLemmatizer()

            TokenizeWordsWithoutStopwords = [word for word in tokens if word not in stop_words]
            return [Lemmatizer.lemmatize(word) for word in TokenizeWordsWithoutStopwords]

        # https://newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
        def CosSimilarity(x, y):
            def squared_sum(x):
                return round(math.sqrt(sum([a * a for a in x])), 3)

            numerator = sum(a * b for a, b in zip(x, y))
            denominator = squared_sum(x) * squared_sum(y)
            return round(numerator / float(denominator), 3)

        sentences = [sentence, pattern]
        sentences = [sent.lower() for sent in sentences]
        sentences = [" ".join(alphabet.Keywords(i)) for i in sentences]
        sentences = [" ".join(Lemmatizer(i)) for i in sentences]

        embeddings = [nlp(sentence).vector for sentence in sentences]
        return CosSimilarity(embeddings[0], embeddings[1])

    # Classify intentions
    def ClassifyIntent(sentence, patterns):
        taglist = [alphabet.CalcCosine(sentence, pattern) for pattern in patterns]

        # return re.findall(r'\w[^\{-\}]*', response) #* Use this when dealing with intent.json file.
        SortedScore = [SentScore for SentScore in sorted(taglist, reverse=True)]
        return SortedScore[0]

    # List out keywords from a sentence.
    def Keywords(Sentence):
        stop_words = set(stopwords.words('english'))
        total_words = Sentence.split()
        total_word_length = len(total_words)

        total_sentences = nltk.tokenize.sent_tokenize(Sentence)
        total_sent_len = len(total_sentences)

        tf_score = {}
        for each_word in total_words:
            each_word = each_word.replace('.','')
            if each_word not in stop_words:
                if each_word in tf_score:
                    tf_score[each_word] += 1
                else:
                    tf_score[each_word] = 1

        tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())

        def check_sent(word, sentences):
            final = [all([w in x for w in word]) for x in sentences]
            sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
            return int(len(sent_len))

        idf_score = {}
        for each_word in total_words:
            each_word = each_word.replace('.','')
            if each_word not in stop_words:
                if each_word in idf_score:
                    idf_score[each_word] = check_sent(each_word, total_sentences)
                else:
                    idf_score[each_word] = 1

        idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
        tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

        def get_top_n(dict_elem, n=None):
            result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n])
            return result

        return list(get_top_n(tf_idf_score).keys())

class Functions:
    # Greet the user according to the current time.
    def GreetUs():
        Hour = int(datetime.datetime.now().hour)
        Template = [[["Good morning sir."]],
                    [["Good afternoon sir."], ["Hope you are having a good day.", "Hope you are enjoying your day.", 12]],
                    [["Good evening sir."], ["Hope you had a good day.", "Hope you enjoyed your day.", 12]]]

        # Greet according to time.
        if Hour >= 4 and Hour < 7:
            # TODO: Make sure it will only greet this way once.
            WeatherDialogues = [1, 2]
            WeatherDialogues.extend([0]*8)
            MorningReport = numpy.random.choice(WeatherDialogues)
            if MorningReport == 1: Functions.WeatherReport()
            elif MorningReport == 2: Functions.WeatherTemp()
            else: Core.Speak(alphabet.ArrangeWords(Template[0]))

        elif Hour >= 0 and Hour < 12: Core.Speak(alphabet.ArrangeWords(Template[0]))
        elif Hour >= 12 and Hour < 18: Core.Speak(alphabet.ArrangeWords(Template[1]))
        else: Core.Speak(alphabet.ArrangeWords(Template[2]))

    # Get the weather report.
    def WeatherReport():
        # https://medium.com/analytics-vidhya/forecast-weather-using-python-e6f5519dc3c1
        City = "Bhagalpur"
        print(f"Displaying weather report for: {City}")

        # Fetch weather details.
        URL = f"https://wttr.in/{City}?format=%C"
        res = requests.get(URL)

        Template = [f"The weather today in {City} is {res.text}.",
                    f"It will be a {res.text} day outside.",
                    f"It will be a {res.text} day in {City}.",
                    f"Today's weather in {City} is {res.text}.",
                    f"The weather outside is {res.text}.",
                    f"The weather in {City} is {res.text}.",
                    f"{City}'s weather is {res.text}."]

        Core.Speak(numpy.random.choice(Template))

    # Get today's temperature.
    def WeatherTemp():
        # Used as reference,
        # https://medium.com/analytics-vidhya/forecast-weather-using-python-e6f5519dc3c1
        City = "Bhagalpur"
        print(F"Displaying temperature in: {City}")

        # Fetch weather details.
        URL = f"https://wttr.in/{City}?format=%t"
        res = requests.get(URL)
        Temp = res.text[1:] if res.text[0] == "+" else res.text

        Template = [f"The temperature today in {City} is {Temp}.",
                    f"Today's temperature in {City} is {Temp}.",
                    f"The temperature outside is {Temp}.",
                    f"The weather outside is {Temp}.",
                    f"The weather in {City} is {Temp}.",
                    f"The temperature in {City} is {Temp}.",
                    f"{City}'s temperature is {Temp}."]

        Core.Speak(numpy.random.choice(Template))

    # Translate to any language
    def Translate(Query):
        #TODO: For now it only translates only to english, change it in future.
        regex = re.findall(r'translate this to english (.*)|translate to english (.*)|translate this (.*)|translate (.*)', Query)
        if regex:
            regex = [j for i in regex for j in list(filter(None, i))]
            Query = str(" ".join(i for i in regex)).strip()

        out = translator.translate(Query, dest="en")
        Core.Speak(out.text)

    # Search and play media on YouTube.
    def PlayOnYT(Query):
        Template = [["As you wish,", "Sure.", "Sure sir,", 12], ["Your results are on your screen.", "Here are your results.", "Here you go.",
        "Searching on YouTube...", "Opening on YouTube...", 18]]

        regex = re.findall(r'play from yt (.*)|search from yt (.*)|search from youtube (.*)|play from youtube (.*)|play on yt (.*)|search on yt (.*)|search on youtube (.*)|play on youtube (.*)|play (.*)', Query)
        if regex:
            regex = [j for i in regex for j in list(filter(None, i))]
            Query = str(" ".join(i for i in regex)).strip()

        pywhatkit.playonyt(Query)
        Core.Speak(alphabet.ArrangeWords(Template))

    # Get the current time
    def GetTime():
        Template = [["Sure", "Sure sir,", 8], ["The time is,", "It's"]]

        Hrs = int(datetime.datetime.now().hour)
        Mins = int(datetime.datetime.now().minute)
        Seconds = int(datetime.datetime.now().second)
        CTime = f"{Hrs}:{Mins}"

        TimeDialogue = [alphabet.ArrangeWords(Template)]
        TimeDialogue.extend([""*8])
        Core.Speak(f"{numpy.random.choice(TimeDialogue)} {CTime}".strip())

    # Create a new project
    def CreateProject(Query):
        # regex = re.findall(r'[create|make|start]* a (.*) (indexed|index it|marked|mark it|named|name it)[ as ]*(.*)', Query)
        Template = [["As you wish", "Here you go", "Sure", 7], ["Sir", 7]]
        regex = re.findall(r'([create|make|start]* a (.*) (indexed|index it|marked|mark it|named|name it)[ as ]*(.*))|[create|make|start]* a (.*)', Query)
        if regex:
            regex = [j for i in regex for j in list(filter(None, i))]
            if not any(i in regex for i in ["indexed", "index it", "marked", "mark it", "named", "name it"]):
                Core.Speak("What shall I name it Sir?")
                proj_name = str(Core.TakeCommand().lower().strip()).capitalize()

            else: proj_name = str(regex[2]).capitalize()

            os.mkdir(f"D:\\Dev Projects\\{proj_name}")

        else:
            Template = [["I'm", "I am", 1], ["Sorry,", "Sorry but", "Sorry sir,", "Sorry sir but"],
                        ["I"], ["failed to", "wasn't able to", "couldn't"], ["create this project."]]

        Core.Speak(alphabet.ArrangeWords(Template))

    # Tell some joke
    def CrackJokes(): Core.Speak(pyjokes.get_joke(language="en", category="all"))

    # Tell some joke
    def Facts(): Core.Speak(randfacts.get_fact())

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

            sentence_list = nltk.tokenize.sent_tokenize(article_text)
            stop_words = stopwords.words('english')

            word_frequencies = {}
            for word in nltk.tokenize.word_tokenize(formatted_article_text):
                if word not in stop_words:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

            maximum_frequncy = max(word_frequencies.values())

            for word in word_frequencies.keys():
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

            sentence_scores = {}
            for sent in sentence_list:
                for word in nltk.tokenize.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]

            summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

            summary = ' '.join(summary_sentences)
            Template = [["Sure,", "Sure sir,", "Here you go,", "Here you go sir,", 18]]

            Core.Speak(alphabet.ArrangeWords(Template))
            Core.Speak(summary)

        # If error caught then search on Google.
        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}{e}")
            Template = [["I'm", "I am", 1], ["Sorry,", "Sorry but", "Sorry sir,", "Sorry sir but"],
                        ["I"], ["failed to", "wasn't able to", "couldn't"], ["summarize.", "summarize you query.", "connect."]]

            print("Failed to connect")
            Core.Speak(alphabet.ArrangeWords(Template))

    # Search on Google or Wikipedia.
    def SearchOnline(Query):
        Template = [["Sure,", "Sure sir,", 12], ["Here you go", "Here's what I found on the web",
                    "Your results are on your screen.", "Here you go.", "Here are your results.", "Google says...",
                    "Searching on Google...", "According to Wikipedia...", "According to Google...", 18]]

        regex = re.findall(r'.* wikipedia for (.*)|.* google for (.*)|search on wikipedia (.*)|search on google (.*)|search for (.*)|search on (.*)|search (.*)', Query)
        if regex:
            regex = [j for i in regex for j in list(filter(None, i))]
            Query = str(" ".join(i for i in regex)).strip()

        # First try searching on Wikipedia.
        try:
            Results = wikipedia.summary(Query, sentences=2)
            pywhatkit.search(Query)
            Core.Speak(alphabet.ArrangeWords(Template))
            Core.Speak(Results)

        # If error caught then search on Google.
        except Exception as e:
            pywhatkit.search(Query)
            print(f"{Fore.RED}{Style.BRIGHT}{e}")
            print("Failed to connect")
            Core.Speak(alphabet.ArrangeWords(Template))

    # Play offline media
    def PlayOfflineMedia(Query):
        # List all the files in the given directory and play them randomly.
        def StartPlaying(Directory):
            Files = os.listdir(Directory)
            Media = os.path.join(Directory, Files[random.randint(0, len(Files)-1)])
            os.startfile(Media)

        Template = [["Sure", "Here you go", "As you wish", 12], ["sir", 5]]
        media = {}

        media["pic"] = alphabet.ClassifyIntent(Query, ["show a picture", "show a pic", "open any pic", "open me some picture", "show a photo", "open any image", "open me some image", "can you please show a photo"])
        media["song"] = alphabet.ClassifyIntent(Query, ["play a song", "hit me with some music", "hit any music" "hit some music", "play me some music", "can you please play a song"])
        media["video"] = alphabet.ClassifyIntent(Query, ["play a video", "play any video", "play me some video", "can you please play a video"])

        media_with_highest_confidence = max(media, key=media.get)

        if media_with_highest_confidence == "song":
            StartPlaying("D\\Srijan\\Music")
            Core.Speak(alphabet.ArrangeWords(Template))

        elif media_with_highest_confidence == "video":
            StartPlaying("D\\Srijan\\Videos")
            Core.Speak(alphabet.ArrangeWords(Template))

        elif media_with_highest_confidence == "pic":
            StartPlaying("D\\Srijan\\Pictures")
            Core.Speak(alphabet.ArrangeWords(Template))

        else:
            Template = [["I'm", "I am", 1], ["Sorry,", "Sorry but", "Sorry sir,", "Sorry sir but"],
                        ["I"], ["failed to", "wasn't able to", "couldn't"], ["follow your query."]]

            print(f"Failed to play '{Query}'")
            Core.Speak(alphabet.ArrangeWords(Template))

    # Close an app.
    def KillTask(Query):
        Apps = []
        UnclosedApps = []
        regex = re.findall(r'.* this app| .* current app|exit (\w+)|kill (\w+)|close (\w+)|quit (\w+)|shutdown (\w+)', Query)
        if regex: Apps = [j for i in regex for j in list(filter(None, i))]

        Core.Speak(alphabet.ArrangeWords([["Sure", "As you wish", "Ok", "Here you go"], ["sir", 2]]))
        if Apps:
            for i in Apps:
                for p in psutil.process_iter():
                    if (i in str(p.name()).lower()):
                        os.system(f"taskkill /f /im {p.name()}")

                    else: UnclosedApps.append(i)

            if Apps != UnclosedApps:
                Template = [["I'm", "I am", 1], ["Sorry,", "Sorry but", "Sorry sir,", "Sorry sir but"],
                            ["I"], ["failed to", "wasn't able to", "couldn't"],
                            ["close", "kill", "shutdown", "exit", "quit"], [', '.join(set(UnclosedApps)) + "."]]

                print(f"Failed to close '{', '.join(set(UnclosedApps))}'")
                Core.Speak(alphabet.ArrangeWords(Template))

        else:
            # https://stackoverflow.com/a/70574370/18121288
            hwnd = pyautogui.getActiveWindow()._hWnd
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)
            process_name = process.name()
            os.system(f"taskkill /f /im {process_name}")

    # Switch window
    def SwitchWindows(Query):
        Template = [["Sure", "As you wish", "Ok", "Here you go", "Switched", 8], ["sir", 12]]

        tasks = list(filter(None, pyautogui.getAllTitles()))
        tasks.remove("Microsoft Text Input Application")
        tasks.remove("Program Manager")

        Apps = []
        regex = re.findall(r'switch to (.*)|switch (.*)|change to (.*)|change (.*)', Query)
        if regex: Apps = [j for i in regex for j in list(filter(None, i))]

        if "window" in Apps or "app" in Apps:
            CurrentTask = pyautogui.getActiveWindowTitle()
            if CurrentTask.lower() in [i.lower() for i in tasks]:
                title = tasks[tasks.index(CurrentTask) + 1]

                pyautogui.keyDown('alt')
                pyautogui.keyDown('tab')
                pyautogui.keyUp('alt')

                Core.Speak(alphabet.ArrangeWords(Template))

        else:
            app_score = [[alphabet.ClassifyIntent(Apps[0], [i]), i] for i in tasks]
            title = sorted(app_score, reverse=True)[0][1]
            idx = tasks.index(title)

            pyautogui.keyDown('alt')
            for _ in range(idx): pyautogui.press('tab')
            pyautogui.keyUp('alt')

            Core.Speak(alphabet.ArrangeWords(Template))

    # Open Sites or Apps
    def OpenSitesOrApps(Query):
        def OpenExtentionFunc(Keyword, Link, OpenWith):
            if Keyword in Query:
                Core.Speak("Please wait..")
                if OpenWith == "search": pywhatkit.search(Link)
                elif OpenWith == "browser": webbrowser.open(Link)
                elif OpenWith == "system": os.startfile(Link)
                else:
                    Template = [["I'm", "I am", 1], ["Sorry", "Sorry,", "Sorry but"],
                                ["I"], ["failed", "wasn't able"], ["to follow your query."]]

                    Core.Speak(alphabet.ArrangeWords(Template))

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

# Setup Terminal
print(f"{Fore.BLUE}{Style.BRIGHT}WINTER")
Core.Speak(Functions.GreetUs())

while True:
    # Take input from the user and do some natural language processing on it.
    # Command = Core.TakeCommand().lower().strip()
    Command = input("> ").lower().strip()
    OriginalSentence = Command

    # regex = re.findall(r'winter (.*)|(.*) winter', Command)
    # if regex:
    #     regex = [j for i in regex for j in list(filter(None, i))]
    #     Command = str(" ".join(i for i in regex)).strip()

    # Identify the best response
    if Command:
        Command = tokenize(Command)
        X = bag_of_words(Command, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]: response = intent['responses']

        else: response = OriginalSentence
    
    # Respond with the appropriate response.
    if response[0] == "": pass
    elif response[0] == "Exit":
        Template = ["Ok sir", "Bye sir"]
        Template.extend([""]*4)

        Core.Speak(numpy.random.choice(Template))
        sys.exit()

    elif response[0] == "Facts": Functions.Facts()
    elif response[0] == "GetTime": Functions.GetTime()
    elif response[0] == "GreetUs": Functions.GreetUs()
    elif response[0] == "WeatherReport": Functions.WeatherReport()
    elif response[0] == "TempReport": Functions.WeatherTemp()
    elif response[0] == "CrackJokes": Functions.CrackJokes()
    elif response[0] == "CreateProject": Functions.CreateProject(OriginalSentence)
    elif response[0] == "KillTask": Functions.KillTask(OriginalSentence)
    elif response[0] == "SearchOnline": Functions.SearchOnline(OriginalSentence)
    elif response[0] == "Summarize": Functions.Summarize(OriginalSentence)
    elif response[0] == "Translate": Functions.Translate(OriginalSentence)
    elif response[0] == "SwitchWindows": Functions.SwitchWindows(OriginalSentence)
    elif response[0] == "OpenSitesOrApps": Functions.OpenSitesOrApps(OriginalSentence)
    elif response[0] == "PlayOnYT": Functions.PlayOnYT(OriginalSentence)
    elif response[0] == "PlayOfflineMedia": Functions.PlayOfflineMedia(OriginalSentence)
    else:
        if isinstance(response, list): Core.Speak(alphabet.ArrangeWords(response))
        else: Functions.SearchOnline(OriginalSentence)
