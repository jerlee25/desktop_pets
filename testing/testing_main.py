from time import sleep, perf_counter
from threading import Thread


# from pet_screen import PetScreen
import tkinter as tk 
from PIL import Image
from PIL import ImageTk
from ahk import AHK

from ahk import AHK
# import ahkpy
import math
import keyboard

print("hi")
ahk = AHK()
def task():
    pass

def task1():
    print("Hi")
    

    sleep(1)
    from ahk_pet_screen_mover import specialWindow
# print("hi")
    # win = ahk.find_window(title='PETSCREEN') # Find the opened window
    # win.always_on_top = 'On'
    # win.set_always_on_top('On')

    # theta = 0
    # win = specialWindow(win)

    # state = 0
    # ttime = 0
   
    # stableTarx = 0
    # stableTary = 0
    # while True:
    #     print('hi')
    #     ttime +=1

    

    #     if (ttime%10==0):
    #         #win.update()
    #         ttime = 0
    #     if keyboard.is_pressed("a"):
    #         state =2
        
    #     if keyboard.is_pressed("ctrl+alt+p"):
    #         get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
    #         stableTarx = get_mouse_pos[0]
    #         stableTary = get_mouse_pos[1]
    #         state = 3
    #     # if state ==1:
    #     #     win.move(x=ahk.get_mouse_position()[0]-win.get_position()[2]/2+math.cos(theta)*250, y=ahk.get_mouse_position()[1]-win.get_position()[3]/2+math.sin(theta)*250,blocking=False);
    #     #     theta+=.07

    #     if state == 2:
    #         #print("hi")
    #         # curx = win.get_position()[2]
    #         # cury = win.get_position()[3]
    #         get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
    #         tarx = get_mouse_pos[0]
    #         tary = get_mouse_pos[1]
    #         # print(get_mouse_pos)
    #         # tarwin = ahk.win_get_from_mouse_position()
    #         # tarwinx= tarwin.get_position()[0]+11
    #         # tarwiny= tarwin.get_position()[1]+11
    #     # print(tarwinx,tarwiny)
            
        
    #         #print(tarx,tarya
    #         # state = 0
    #         win.moveTowards(tarx,tary)
    #         # win.moveTowards(tarx+tarwinx,tary+tarwiny)aaaa
    #     if state ==3:
    #         win.moveTowards(stableTarx,stableTary)
            

            


    # ahk.add_hotkey('^+LButton', callback=my_callback)
    # ahk.start_hotkeys()  # start the hotkey process thread
    # ahk.block_forever()  
    # ahk.add_hotstring('btw', my_callback) # call python function in response to the hotstring

   

def task2():
    print("hi2")
    from pet_screen import PetScreen
    

start_time = perf_counter()

# create two new threads
t1 = Thread(target=task1)
t2 = Thread(target=task2)

t2.start()
t1.start()


# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')