import random

import pyautogui as pg
import time

animal= ('monkey','donkey','dog')

time.sleep(8)
for i in range(500):
 a=random.choice(animal)
 pg.write("I love u😘")
 pg.press('enter')