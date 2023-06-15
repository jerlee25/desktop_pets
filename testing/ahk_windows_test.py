from ahk import AHK
# import ahkpy
import math
import keyboard
import time


ahk = AHK()


time.sleep(1)
print("hi")
win = ahk.find_window(title='PETSCREEN') # Find the opened window
win.always_on_top = 'On'
win.set_always_on_top('On')

theta = 0
class specialWindow:
    def __init__(self,win):
        self.win = win
        self.x = self.win.get_position()[0]
        self.y = self.win.get_position()[1]
        self.speed = 20
        self.acceleration = 0
        self.dx = 0
        self.dy = 0
        self.width = win.get_position()[2]
        self.height = win.get_position()[3]
        self.hw=win.get_position()[2]/2
        self.hh = win.get_position()[3]/2
        # self.ddx = 0
        # self.ddy = 0
    def updatePos(self):
        # self.dx += self.ddx
        # self.dy += self.ddy
        self.x += self.dx
        self.y += self.dy
        print("dx",self.dx,"dy",self.dy)
        self.win.move(x=self.x,y=self.y,blocking=True)
        print(self.x,self.y)
    def update(self):
        self.x = self.win.get_position()[0]
        self.y = self.win.get_position()[1]
        self.updatePos()
        print("hi")
    def moveTowards(self,tarx,tary):
        
        xChange = self.x+self.hw-tarx
        yChange = self.y+self.hh-tary
        otherChange = math.sqrt(xChange**2+yChange**2)
        if otherChange >100:
            self.acceleration +=.25
        elif otherChange >10:
            self.acceleration -=.05
        else:
            self.acceleration -=.5
        
        self.acceleration = min(1,self.acceleration)
        self.acceleration = max(0,self.acceleration)
        
        self.dx = -self.acceleration * self.speed * xChange/otherChange
        self.dy = -self.acceleration * self.speed * yChange/otherChange
        self.updatePos()
        #print("dx",self.dx,"dy",self.day)
        


win = specialWindow(win)

state = 0
ttime = time
time = 0
while True:
    
    time +=1
    if (time%10==0):
        #win.update()
        time = 0
    if keyboard.is_pressed("a"):
        state =2
      
    
    # if state ==1:
    #     win.move(x=ahk.get_mouse_position()[0]-win.get_position()[2]/2+math.cos(theta)*250, y=ahk.get_mouse_position()[1]-win.get_position()[3]/2+math.sin(theta)*250,blocking=False);
    #     theta+=.07

    if state == 2:
        #print("hi")
        # curx = win.get_position()[2]
        # cury = win.get_position()[3]
        tarx = ahk.get_mouse_position()[0]
        tary = ahk.get_mouse_position()[1]
        #print(tarx,tary)
        # state = 0
        win.moveTowards(tarx,tary)
        

        


# ahk.add_hotkey('^+LButton', callback=my_callback)
# ahk.start_hotkeys()  # start the hotkey process thread
# ahk.block_forever()  
# ahk.add_hotstring('btw', my_callback) # call python function in response to the hotstring
