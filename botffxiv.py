import time
import pynput.mouse as ms
import pynput.keyboard as kb
import random
import mss
import cv2
import numpy as np
import threading
from colorama import Fore
mouse = ms.Controller()
keyboard = kb.Controller()
def coutdown():
    global secondes
    global minutes
    global heures
    secondes = 0
    minutes = 0
    heures = 0
    while True:
        secondes = secondes + 1
        time.sleep(1)
        if secondes == 60:
            secondes = 0
            minutes = minutes + 1
        if minutes == 60:
            secondes = 0
            minutes = 0
            heures = heures + 1


countdown_thread = threading.Thread(target=coutdown)
countdown_thread.start()

def pause():
    time.sleep(random.uniform(0.5, 0.7))


def bougersouris(x, y):
    mouse.position = (x + random.randint(-3, 3), y + random.randint(-3, 3))
    pause()


def clique():
    mouse.press(ms.Button.left)
    time.sleep(random.uniform(0.01, 0.02))
    mouse.release(ms.Button.left)
    time.sleep(random.uniform(0.01, 0.02))


def cliquedroit():
    time.sleep(random.uniform(0.01, 0.06))
    mouse.press(ms.Button.right)
    time.sleep(random.uniform(0.01, 0.06))
    mouse.release(ms.Button.right)
    time.sleep(random.uniform(0.01, 0.06))


def test():
    monitor = {"top": 942, "left": 887, "width": 30, "height": 20}
    monitor2 = {"top": 940, "left": 805, "width": 30, "height": 20}

    low_white = np.array([250, 240, 240])
    high_white = np.array([255, 255, 255])

    low_1er = np.array([0, 60, 60])
    high_1er = np.array([75, 255, 255])

    succes = True
    test = True
    aaaa = False

    with mss.mss() as sct:
        while aaaa == False:
            img = np.array(sct.grab(monitor))
            img2 = np.array(sct.grab(monitor2))
            rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            rgb_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

            maskw = cv2.inRange(rgb_image, low_white, high_white)
            maskw2 = cv2.inRange(rgb_image2, low_1er, high_1er)

            cordsr = []
            cordsr2 = []

            yw, xw = np.where(maskw != 0)
            yw2, xw2 = np.where(maskw2 != 0)
            if test:
                for i in range(len(yw2)):
                    cordsr2.append([yw2[i], xw2[i]])
                    test = False
                    succes = False
                    break
            if not succes:
                for i in range(len(yw)):
                    cordsr.append([yw[i], xw[i]])
                    succes = True
                    clique()
                    aaaa = True
                    break


i = 0
while True:
    i = i + 25
    bougersouris(958, 547)
    cliquedroit()
    pause()
    bougersouris(819, 558)
    clique()
    pause()
    bougersouris(1224, 939)
    test()
    print(f"{Fore.GREEN}En tout , tu as collecté : {Fore.RESET}" + str(i) + f"{Fore.RED} PGS {Fore.RESET}"+"et tout ça en "+str(heures)+"H "+str(minutes)+"M "+str(secondes)+"S")
    time.sleep(random.randint(5, 6))
