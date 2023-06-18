from time import sleep, perf_counter
from threading import Thread


# from pet_screen import PetScreen
import tkinter as tk 
from PIL import Image
from PIL import ImageTk
from ahk import AHK
from playsound import playsound
from ahk import AHK
import math
import keyboard


ahk = AHK()


# Class that can store information between the two threads
class UsefulInfo():
    def __init__(self):
        self.isMoving = 0


# Run screen mover code (originally from ahk_pet_screen_mover.py)

def ahkScreenMover(info):
    
    
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
            self.x = self.win.get_position()[0]
            self.y = self.win.get_position()[1]
            self.speed = 50
            self.acceleration = 0
            self.dx = 0
            self.dy = 0
            self.width = win.get_position()[2]
            self.height = win.get_position()[3]

            # half height and half width because I didn't want to do too much math like elsewhere

            self.hw=win.get_position()[2]/2
            self.hh = win.get_position()[3]/2
            
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
    win = specialWindow(or_win,info)


    # Tracking type of movement I think
    state = 0
   

    # targetting a speciic location that doesn't change

    stableTarx = 0
    stableTary = 0

    # Probably a cleaner way to this than a while loop, but moving windows is already slow as is

    while or_win.exists():
        
     


        # Keybinds for speeding up the window's speed

        if keyboard.is_pressed("ctrl+alt+up"):
            win.speed+=10
        if keyboard.is_pressed("ctrl+alt+down"):
            win.speed-=10

        win.speed = min(200,win.speed)
        win.speed = max(20,win.speed)
     


         # Set to follow mouse

        if keyboard.is_pressed("ctrl+alt+a"):
            state =2
        
        # Go to the position mouse is currently at at that moment but not like follow just record it and go there

        if keyboard.is_pressed("ctrl+alt+p"):
            get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
            stableTarx = get_mouse_pos[0]
            stableTary = get_mouse_pos[1]
            state = 3
        if keyboard.is_pressed("ctrl+alt+q"):

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
            

    


    

# Run pet screen code (originally from pet_screen.py)
    
def runPetScreen(info):
    
    # Make the pet screen, take in an info object for communication
    
    class PetScreen(tk.Frame):
    
        def __init__(self, master,info):

            # Set a certain size, not exactly sure how to use tkinter properly, just took old code and messed with it until it worked

            super().__init__(master,width=150,height=150)
            self.grid()
            self.info = info

            # Because it starts by incrementing it in the code so we start at -1 so it goes to 0 haha

            self.thing =  -1
          

            # 0 - idle
            # 1 - move
            # 2 - happy
            # 3 - sleep
            self.state_names = ["idle","move","happy","sleep","still"]


            # Order of frames for each state in each array in each tuple
            # First thing in each tuple is like delay before changing

            self.orders = [(2,[0,1,0,2]),(2,[0,1]),(2,[0,1,2,3,3]),(2,[0,1,2,3,3]),(2,[0])]

            # Recording state stuff

            self.isHappy = 0
            self.isAsleep = 0
            self.state = 0
            self.hasBeenMoving = 0
            self.pet_names = ["orange_cat","grey_cat","emelem_cat"]
            self.which_pet = 2


            # Creating label before hand so we don't create a bunch of labels and crash

            img_original = Image.open("images/"+self.pet_names[self.which_pet]+"/idle_0.png")
            
            img_original = img_original.resize((150, 150), Image.ANTIALIAS)
            
            
            img = ImageTk.PhotoImage(img_original)
            self.lbl = tk.Label(self, image = img)
            self.lbl.image = img
            self.lbl.grid(row=0, column = 0, columnspan = 1)

            # Reactions to being clicked and stuff

            def beHappy(event):
               
                if (self.info.isMoving==0):
                    self.state = 2
                    self.thing = -1
                    def play_sound():
                        playsound("images/"+self.pet_names[self.which_pet]+"/meow.mp3")
                    thread = Thread(target=play_sound)
                    thread.start()
            
            def beSleep(event):
              
                if (self.info.isMoving==0):
                    self.state = 3
                    self.thing = -1
                    def play_sound():
                        playsound("images/"+self.pet_names[self.which_pet]+"/purr.mp3")
                    thread = Thread(target=play_sound)
                    thread.start()
            def beStill(event):
               
                if (self.info.isMoving==0):
                    self.state = 4
                    self.thing = -1
            def changeCat(event):
                self.which_pet += 1
                self.which_pet %= len(self.pet_names)

            # Binding stuff to keybinds which is a bit weird with tkinter but this works so I'm not touching it
            
            self.lbl.bind("<Button-1>", beHappy)
            self.lbl.bind("<Shift-Button-1>", beSleep)
            self.lbl.bind("<Control-Button-1>", beStill)
            self.lbl.bind("<Shift-Control-Button-1>", changeCat)

            # Run the repeating loop

            self.dance() 

        
   
          
        # The repeatng loop

        def dance(self):
          
            
            # Checks for when it starts moving and stops moving and just moving stuff in general

            if (self.hasBeenMoving ==0 and self.info.isMoving ==1):
                self.hasBeenMoving =1
                self.thing = -1
                self.state  = 1
            if self.hasBeenMoving ==1 and self.info.isMoving == 0 and self.state ==1:
                self.hasBeenMoving = 0
                self.thing = -1
                self.state = 0
            if self.info.isMoving==1:
                self.state = 1
           
            # Iterating

            self.thing+=1
           
            # Cycling like a bicycle but not actually
            # Does a bit of stuff with the orders to just find the next frame and when it changes that
            # Threw this together like instinctively and it sort of just worked so I'm keeping it like that

            cur_order= self.orders[self.state]
            cycle_len = cur_order[0] * len(cur_order[1])
            if self.state == 2 and self.thing ==cycle_len:
                self.state = 0
            self.thing %= cycle_len
            index = self.thing // cur_order[0]

            img_original = Image.open("images/"+self.pet_names[self.which_pet]+"/" + self.state_names[self.state]+"_"+str(cur_order[1][index])+".png")
            
            img_original = img_original.resize((150, 150), Image.ANTIALIAS)
            
            img = ImageTk.PhotoImage(img_original)
           
            self.lbl.configure(image=img)
            self.lbl.image = img
        
            # Calls itself again

            self.after(100, self.dance)

        

        



    # Idk a bunch of tkinter stuff that makes it work ig

    root =tk.Tk()

    root.title('PETSCREEN')

    view = PetScreen(root,info)
    root.resizable(False,False)

    root.mainloop()







# Tracking time that the threading thing I looked at had and I'm keeping it because it's fun

start_time = perf_counter()


stuff = UsefulInfo()
t1 = Thread(target=lambda:ahkScreenMover(stuff))
t2 = Thread(target=lambda:runPetScreen(stuff))

t2.start()
t1.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')