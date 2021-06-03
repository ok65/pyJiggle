
import pyautogui
import time
import random

mouse_pos = pyautogui.position()

while True:
    time.sleep(5)
    if mouse_pos == pyautogui.position():
        pyautogui.move(random.randint(-10, 10), random.randint(-10, 10))
        print("jiggle")
    mouse_pos = pyautogui.position()
