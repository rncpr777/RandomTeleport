import pyautogui
import time
import random

pyautogui.moveTo((990, 1050))
pyautogui.click()
pyautogui.moveTo((900, 450))
time.sleep(1)
pyautogui.click()
pyautogui.typewrite('Google Maps')
pyautogui.press('enter')
pyautogui.moveTo((300, 330))
time.sleep(1)
pyautogui.click()
pyautogui.moveTo((110, 110))
a = random.randrange(1, 99)
a1 = random.randrange(0, 99999)
b = random.randrange(1, 99)
b1 = random.randrange(0, 99999)
a = str(a) + '.' + str(a1)
b = str(b) + '.' + str(b1)
ins = a + ', ' + b
time.sleep(1)
pyautogui.typewrite(ins)
pyautogui.moveTo((300, 180))
time.sleep(1)
pyautogui.click()
pyautogui.moveTo((550, 1000))
time.sleep(1)
pyautogui.click()