import pyautogui
from pynput.keyboard import Key, Controller
import keyboard as kb
import pyperclip
import time
from time import sleep
import ocr_example

keyboard = Controller()
x, y = 936, 460

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

# Engine Timings
# 1 - 1.834 - Acc(50%) 1200000
# 2 - 2.218 - Acc(85%) 165000
# 3 - 4.654 - Acc(70%) 1094
# 5 - 5.88  - Acc(98%) 502

while True:
    sleep(0.05)
    if kb.is_pressed('f4') == True:
        while True:
            if pyautogui.pixel(940,400)[0] in range(196,202) or pyautogui.pixel(1150,400)[0] in range(200,210):
                get_text(x,y)
                url = pyperclip.paste()
                pyautogui.click(x,y+100)
                time_start=time.time()
                ocr_text = ocr_example.get_ocr_results(url,5)
                time_end=time.time()
                print(ocr_text)
                print(f"\nTook {time_end-time_start}secs to convert the text.")
                keyboard.type(ocr_text)
                kb.press('tab+enter')
                break
        