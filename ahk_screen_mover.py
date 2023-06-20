import math
import tkinter as tk
from threading import Thread
from time import perf_counter, sleep

import keyboard
from ahk import AHK
from PIL import Image, ImageTk
from playsound import playsound

from keybinds import *

ahk = AHK()

# Run screen mover code (originally from ahk_pet_screen_mover.py)

def ahkScreenMover():
    # Waiting for other screen to appear

    sleep(1)
   
    # Finding the window that we're going to be moving, settting it to the top always

    or_win = ahk.find_window(title='PETSCREEN') 
    or_win.always_on_top = 'On'
    or_win.set_always_on_top('On')

    # Special window class to do stuff since idk how the normal window class works
    class specialWindow:
        def __init__(self,win,info):

            # info stores the special info class for communication

            self.info = info

            # Most of this is like self explanatory

            self.win = win
            win_pos = self.win.get_position()
            self.x = win_pos[0]
            self.y = win_pos[1]
            self.speed = 50
            self.acceleration = 0
            self.dx = 0
            self.dy = 0
            
            
            self.width = win_pos[2]
            self.height = win_pos[3]

            # half height and half width because I didn't want to do too much math like elsewhere
            
            self.hw=win_pos[2]/2
            self.hh = win_pos[3]/2
            
        def updatePos(self):
           
            # Moves to new projected location

            self.x += self.dx
            self.y += self.dy

            self.win.move(x=self.x,y=self.y,blocking=True)
            
        def update(self):

            # Gets actual location, then updates it

            self.x = self.win.get_position()[0]
            self.y = self.win.get_position()[1]
            self.updatePos()
            
        def moveTowards(self,tarx,tary):

            # Updating size if size was updated
            win_pos = win.win.get_position()
            self.x = win_pos[0]
            self.y = win_pos[1]
         
            self.width = win_pos[2]
            self.height = win_pos[3]
            self.hw=win_pos[2]/2
            self.hh = win_pos[3]/2
            
            # Target a thing so that the center of the window starts moving towards a certain point

            xChange = self.x+self.hw-tarx
            yChange = self.y+self.hh-tary
            otherChange = math.sqrt(xChange**2+yChange**2)
            if otherChange >max(self.speed*self.acceleration,25):
                self.acceleration +=.25
            elif otherChange >self.speed/2:
                self.acceleration -=.05
            else:
                self.acceleration -=.5
            
            self.acceleration = min(1,self.acceleration)
            self.acceleration = max(0,self.acceleration)
            if (self.acceleration>0):
                self.info.isMoving = 1
            else:
                self.info.isMoving = 0
            
            self.dx = -self.acceleration * self.speed * xChange/otherChange
            self.dy = -self.acceleration * self.speed * yChange/otherChange
            self.updatePos()

    # Passes in the original window + the info object
    win = specialWindow(or_win)

    # Tracking type of movement I think
    state = 0
   
    # targetting a speciic location that doesn't change

    stableTarx = 0
    stableTary = 0

    curdx = 0
    curdy = 0

    # Get size of screen

    root =tk.Tk()
    screen_width = 2256
    screen_height = 1504

    # Ok for some reason when I run these things it changes the size of the other window?
    # Which is a bit odd, maybe weird things for connecting too each other?
    # So I'm just going to have a defauly screen width and height cause that works well enough and can be changed easily enough

    # for m in get_monitors():
        
    #     screen_width = m.width
    #     screen_height = m.height
    # screen_width, screen_height = pyautogui.size()

    # Probably a cleaner way to this than a while loop, but moving windows is already slow as is

    while or_win.exists():

        # Keybinds for speeding up the window's speed

        if keyboard.is_pressed(SPEED_UP_KEYS):
            win.speed+=10
        if keyboard.is_pressed(SPEED_DOWN_KEYS):
            win.speed-=10

        win.speed = min(200,win.speed)
        win.speed = max(20,win.speed)
     
         # Set to follow mouse
        if keyboard.is_pressed(STOP_THERE_KEYS):
            state = 0
            win.info.isMoving = 0
            
        if keyboard.is_pressed(FOLLOW_MOUSE_KEYS):
            state =2
        
        # Go to the position mouse is currently at at that moment but not like follow just record it and go there

        if keyboard.is_pressed(GO_TO_POSITION_KEYS):
            get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
            stableTarx = get_mouse_pos[0]
            stableTary = get_mouse_pos[1]
            
            state = 3

        # Screensaver code I think

        if keyboard.is_pressed(BECOME_SCREENSAVER_KEYS):
            get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")

            tarx = get_mouse_pos[0]
            tary = get_mouse_pos[1]

            xChange = win.x+win.hw-tarx
            yChange = win.y+win.hh-tary

            otherChange = math.sqrt(xChange**2+yChange**2)

            curdx = -1 * win.speed * xChange/otherChange
            curdy = -1* win.speed * yChange/otherChange

            state = 4
            win.info.isMoving = 0

        if keyboard.is_pressed(QUIT_KEYS):

            # :(

            or_win.kill()
     
        # Move towards mouse's current location
        if state == 2:
          
            get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
            tarx = get_mouse_pos[0]
            tary = get_mouse_pos[1]
            
            win.moveTowards(tarx,tary)
        
        # Move towards that one recorded spot

        if state ==3:
           
            win.moveTowards(stableTarx,stableTary)

        if state ==4:
            win_pos = win.win.get_position()
            win.x = win_pos[0]
            win.y = win_pos[1]
         
            win.width = win_pos[2]
            win.height = win_pos[3]
            win.hw=win_pos[2]/2
            win.hh = win_pos[3]/2
            # print(win.x,win.y)
            win.x += curdx
            win.y += curdy
            if (win.x<0):
                win.x = 2*0-win.x
                curdx = -curdx
            if (win.y <0):
                win.y = 2*0-win.y
                curdy = -curdy
            if (win.x +2*win.hw>screen_width):
                win.x = 2*screen_width - win.x -4*win.hw
                curdx = -curdx
            if (win.y +2*win.hh>screen_height):
                win.y = 2*screen_height - win.y -4*win.hh
                curdy = -curdy

            win.win.move(x=win.x,y=win.y,blocking=True)