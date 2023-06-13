from ahk import AHK
# import ahkpy
import time

ahk = AHK()


time.sleep(1)
win = ahk.find_window(title='PETSCREEN') # Find the opened window
win.always_on_top = 'On'
win.set_always_on_top('On')



def my_callback():
    while True:
        win.move(x=ahk.get_mouse_position()[0]-win.get_position()[2]/2, y=ahk.get_mouse_position()[1]-win.get_position()[3]/2,blocking=False);
    


ahk.add_hotkey('LButton', callback=my_callback)
ahk.start_hotkeys()  # start the hotkey process thread
ahk.block_forever()  
# ahk.add_hotstring('btw', my_callback) # call python function in response to the hotstring
