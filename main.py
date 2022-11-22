import pyautogui
from pynput.keyboard import Key, Controller
import keyboard as kb
import pyperclip
import time
import random
from time import sleep
import ocr_api

keyboard = Controller()
# Change x and y coor around the middle
x, y = 936, 460

# Engine Timings
# 1 - 1.834 - Acc(50%) 1200000
# 2 - 2.218 - Acc(85%) 165000
# 3 - 4.654 - Acc(70%) 1094
# 5 - 5.88  - Acc(98%) 502
engine = 5

# Random enough ;)
fastTestSpeed_rand1 = 0.04
fastTestSpeed_rand2 = 0.08
FastSlowSpeed_rand1 = 0.08
SlowestSpeed_rand2 = 0.12

def get_text(x,y):
    pyautogui.click(x,y, button='right')
    pyautogui.click(x+70,y+85)

def check_captcha_results() -> bool:
    pyautogui.click(x,y-448)
    kb.press('ctrl+c')
    if 'Sorry' in pyperclip.paste():
        return False
    else:
        return True

def get_random_f():
    f = random.uniform(fastTestSpeed_rand1, fastTestSpeed_rand2)
    return f


def get_random_g():
    g = random.uniform(FastSlowSpeed_rand1, SlowestSpeed_rand2)
    return g


def typer():
    for t in txt:
        x = random.uniform(get_random_f(), get_random_g()) 
        keyboard.press(t)
        sleep(x)
        keyboard.release(t)


while True:
    sleep(0.05)
    #Captcha solver 
    if kb.is_pressed('f4') == True:
        while True:
            # Get the coord for captcha using displayMouseLocation() and check their RGB values
            #                  (middle)             (Red range)                (top right corner)    (Red value)
            if pyautogui.pixel(940,400)[0] in range(196,202) or pyautogui.pixel(1150,400)[0] in range(200,210):
                get_text(x,y)
                url = pyperclip.paste()
                pyautogui.click(x,y+130)
                time_start=time.time()
                ocr_text = ocr_api.get_ocr_results(url,engine)
                time_end=time.time()
                print(ocr_text)
                print(f"Took {time_end-time_start}secs to convert the text.\n")
                keyboard.type(ocr_text)
                keyboard.press(Key.tab)
                sleep(0.001)
                keyboard.press(Key.enter)
                sleep(0.001)
                keyboard.release(Key.tab)
                keyboard.release(Key.enter)
                break
    #Types at 125wpm any copied text
    if kb.is_pressed('f2'):
        txt = pyperclip.paste()
        typer()
        
