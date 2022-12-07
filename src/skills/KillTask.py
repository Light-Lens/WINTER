import sys
sys.path.append("..")

import win32gui, win32process, pyautogui, psutil, os
from src.nltk_utils import ClassifyIntent

# Close an app.
def KillTask(appname):
    score = ClassifyIntent(appname, ["current tab", "current app", "this app", "this tab", "current window", "this window", "this window"])
    if score[0] > 0.8:
        if "tab" in score[1]: appname = "_tab"
        elif "app" in score[1] or "window" in score[1]: appname = "_currentapp"

    if appname == "_tab": pyautogui.hotkey('ctrl', 'w')
    elif appname == "_currentapp":
        # https://stackoverflow.com/a/70574370/18121288
        hwnd = pyautogui.getActiveWindow()._hWnd
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        os.system(f"taskkill /f /im {process_name}")

    else:
        tasks = list(filter(None, pyautogui.getAllTitles()))
        tasks.remove("Microsoft Text Input Application")
        tasks.remove("Program Manager")

        app_score = ClassifyIntent(appname, tasks)
        if not app_score: return ""

        title = app_score[1]
        app = pyautogui.getWindowsWithTitle(title)[0].title

        hwnd = win32gui.FindWindow(None, app)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        os.system(f"taskkill /f /im {process_name}")
    return ""
