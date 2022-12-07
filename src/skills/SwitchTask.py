import sys
sys.path.append("..")

import pyautogui
from src.nltk_utils import ClassifyIntent

# Switch window
def SwitchTask(appname):
    score = ClassifyIntent(appname, ["current tab", "current app", "this app", "this tab", "current window", "this window", "this window"])
    if score[0] > 0.8:
        if "tab" in score[1]: appname = "_tab"
        elif "app" in score[1] or "window" in score[1]: appname = "_currentapp"

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

    return ""
