"""Este programa mueve el  raton un poco cada diez segundos para evitar qe el pc see suspenda"""

import pyautogui

while True:
    pyautogui.sleep(10)
    pyautogui.move(2,2,duration=0.10)
    pyautogui.move(-2, -2, duration=0.10)