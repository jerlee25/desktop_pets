import math
import tkinter as tk
from threading import Thread
# from time import perf_counter, sleep

import keyboard
from ahk import AHK
from PIL import Image, ImageTk
from playsound import playsound

import ahk_screen_mover
import menu
import pet_screen

# import pyautogui
# from screeninfo import get_monitors

# Class that can store information between the two threads
class UsefulInfo():
    def __init__(self):
        self.isMoving = 0

# Tracking time that the threading thing I looked at had and I'm keeping it because it's fun

# start_time = perf_counter()

# stuff = UsefulInfo()
# t1 = Thread(target=lambda:ahk_screen_mover.ahkScreenMover(stuff))
# t2 = Thread(target=lambda:pet_screen.runPetScreen(stuff))

# t2.start()
# t1.start()

# t1.join()
# t2.join()

# end_time = perf_counter()

# print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

stuff = UsefulInfo()
menu.run_menu(stuff)