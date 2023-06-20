import tkinter as tk
from threading import Thread

from ahk import AHK
from PIL import Image, ImageTk
from playsound import playsound

import ahk_screen_mover
from keybinds import *

# Make the pet screen, take in an info object for communication

def runPetScreen(info):
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

            self.petSize = 200
            self.isHappy = 0
            self.isAsleep = 0
            self.state = 0
            self.hasBeenMoving = 0
            self.pet_names = [["orange_cat","grey_cat","emelem_cat"],["brown_dog","orange_dog"],["grey_bunny","brown_bunny"]]
            self.which_pet = 0
            self.which_variant = 0


            # Creating label before hand so we don't create a bunch of labels and crash
            

            img_original = Image.open("images/"+self.pet_names[self.which_pet][self.which_variant]+"/idle_0.png")
            
            img_original = img_original.resize((self.petSize, self.petSize))
            
            
            img = ImageTk.PhotoImage(img_original)
            self.lbl = tk.Label(self, image = img)
            # self.lbl.image = img
            self.lbl.grid(row=0, column = 0, columnspan = 1)

            # Reactions to being clicked and stuff

            def beHappy(event):
                
                if (self.info.isMoving==0):
                    self.state = 2
                    
                    self.thing = -1
                    def play_sound():
                        playsound("images/"+self.pet_names[self.which_pet][self.which_variant]+"/meow.mp3")
                    thread = Thread(target=play_sound)
                    thread.start()
            
            def beSleep(event):
                if self.state==3:
                    self.state = 0
                    self.thing = -1
                elif (self.info.isMoving==0):
                    self.state = 3
                    self.thing = -1
                    def play_sound():
                        playsound("images/"+self.pet_names[self.which_pet][self.which_variant]+"/purr.mp3")
                    thread = Thread(target=play_sound)
                    thread.start()
            def beStill(event):
                if (self.state == 4):
                    self.state = 0
                    self.thing = -1
                elif (self.info.isMoving==0):
                    self.state = 4
                    self.thing = -1
                
            def beBig(event):
                self.petSize += 10
                self.petSize = min(self.petSize,900)
                print(self.petSize)
            
            def beSmall(event):
                self.petSize -= 10
                self.petSize = max(self.petSize,130)
                print(self.petSize)

            def changePet(event):
                self.which_pet += 1
                self.which_pet %= len(self.pet_names)
                self.which_variant =0
            
            def changeVariant(event):
                self.which_variant += 1
                self.which_variant %= len(self.pet_names[self.which_pet])

            # Binding stuff to keybinds which is a bit weird with tkinter but this works so I'm not touching it
            
            self.lbl.bind(MAKE_HAPPY_KEYS, beHappy)
            self.lbl.bind(MAKE_SLEEPY_KEYS, beSleep)
            self.lbl.bind(MAKE_STILL_KEYS, beStill)
            self.lbl.bind(MAKE_BIG_KEYS, beBig)
            self.lbl.bind(MAKE_SMALL_KEYS, beSmall)
            self.lbl.bind(CHANGE_PET_KEYS, changePet)
            self.lbl.bind(CHANGE_VARIANT_KEYS, changeVariant)

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

            img_original = Image.open("images/"+self.pet_names[self.which_pet][self.which_variant]+"/" + self.state_names[self.state]+"_"+str(cur_order[1][index])+".png")
            
            img_original = img_original.resize((self.petSize, self.petSize))
            
            img = ImageTk.PhotoImage(img_original)
            
            self.lbl.configure(image=img)
            self.lbl.image = img
        
            # Calls itself again

            self.after(100, self.dance)




    root = tk.Tk()

    root.title('PETSCREEN')

    view = PetScreen(root, info)
    root.resizable(False,False)

    root.mainloop()
    ahk_screen_mover.ahkScreenMover()
