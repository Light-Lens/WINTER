import pyautogui

# Mute the system audio
def MutePC():
    pyautogui.press("volumemute")
    return ""
