import time
import webbrowser
import pygetwindow as gw
import pyautogui
from config import GAME_URL, WEB_RATIO, WINDOW_TITLE_KEYS


def open_game_left():
    webbrowser.open(GAME_URL)
    time.sleep(5)

    screen_w, screen_h = pyautogui.size()

    for title in gw.getAllTitles():
        if any(k in title for k in WINDOW_TITLE_KEYS):
            win = gw.getWindowsWithTitle(title)[0]
            win.restore()
            win.moveTo(0, 0)
            win.resizeTo(int(screen_w * WEB_RATIO), screen_h)
            break
