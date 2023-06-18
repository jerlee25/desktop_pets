from time import sleep, perf_counter
from threading import Thread


# from pet_screen import PetScreen
import tkinter as tk 
from PIL import Image
from PIL import ImageTk
from ahk import AHK
from playsound import playsound
from ahk import AHK
# import ahkpy
import math
import keyboard

print("hi")
ahk = AHK()

class UsefulInfo():
    def __init__(self):
        self.isMoving = 0

def task():
    pass

def ahkScreenMover(info):
    print("Hi")
    

    sleep(1)
    # from ahk_pet_screen_mover import specialWindow
    # ahk = AHK()


# time.sleep(1)
# print("hi")
    or_win = ahk.find_window(title='PETSCREEN') # Find athe opened window
    or_win.always_on_top = 'On'
    or_win.set_always_on_top('On')

    theta = 0
    class specialWindow:
        def __init__(self,win,info):
            self.info = info
            self.win = win
            self.x = self.win.get_position()[0]
            self.y = self.win.get_position()[1]
            self.speed = 50
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
            #"dx",self.dx,"dy",self.dy)
            self.win.move(x=self.x,y=self.y,blocking=True)
            #print(self.x,self.y)
        def update(self):
            self.x = self.win.get_position()[0]
            self.y = self.win.get_position()[1]
            self.updatePos()
            #print("hi")aaaaaa
        def moveTowards(self,tarx,tary):
            
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
            #print("dx",self.dx,"dy",self.day)
            


    win = specialWindow(or_win,info)

    state = 0

    ttime = 0
    stableTarx = 0
    stableTary = 0
    while or_win.exists():
        
        ttime +=1


        if keyboard.is_pressed("ctrl+alt+up"):
            win.speed+=10
        if keyboard.is_pressed("ctrl+alt+down"):
            win.speed-=10
        win.speed = min(200,win.speed)
        win.speed = max(20,win.speed)
        # print(win.speed)a
        
        if (ttime%10==0):
            #win.update()aaaaa
            ttime = 0
        if keyboard.is_pressed("ctrl+alt+a"):
            state =2
        
        if keyboard.is_pressed("ctrl+alt+p"):
            get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
            stableTarx = get_mouse_pos[0]
            stableTary = get_mouse_pos[1]
            state = 3
        if keyboard.is_pressed("ctrl+alt+q"):

            # :(

            or_win.kill()


        # if state ==1:
        #     win.move(x=ahk.get_mouse_posaaition()[0]-win.get_position()[2]/2+math.cos(theta)*250, y=ahk.get_mouse_position()[1]-win.get_position()[3]/2+math.sin(theta)*250,blocking=False);
        #     theta+=.07

        if state == 2:
            #print("hi")
            # curx = win.get_position()[2]
            # cury = win.get_position()[3]
            get_mouse_pos = ahk.get_mouse_position(coord_mode="Screen")
            tarx = get_mouse_pos[0]
            tary = get_mouse_pos[1]
            # print(get_mouse_pos)
            # tarwin = ahk.win_get_from_mouse_position()
            # tarwinx= tarwin.get_position()[0]+11
            # tarwiny= tarwin.get_position()[1]+11
        # print(tarwinx,tarwiny)
            
        
            #print(tarx,tarya
            # state = 0
            win.moveTowards(tarx,tary)
            # win.moveTowards(tarx+tarwinx,tary+tarwiny)aaaa
        if state ==3:
            win.moveTowards(stableTarx,stableTary)
            

            


    # ahk.add_hotkey('^+LButton', callback=my_callback)
    # ahk.start_hotkeys()  # start the hotkey process thread
    # ahk.block_forever()  
    # ahk.add_hotstring('btw', my_callback) # call python funaction in response to the hotstring


    


    
def runPetScreen(info):
    print("hi2")
    # from pet_screen import PetScreen
    
    class PetScreen(tk.Frame):
    
        def __init__(self, master,info):

            super().__init__(master,width=150,height=150)
            self.grid()
            self.info = info
            self.thing =  -1
            # self.create_widgets()
            
            # self.last_loc = (0,0)

            # 0 - idle
            # 1 - move
            # 2 - happy
            # 3 - sleep
            self.state_names = ["idle","move","happy","sleep","still"]


            self.orders = [(2,[0,1,0,2]),(2,[0,1]),(2,[0,1,2,3,3]),(2,[0,1,2,3,3]),(2,[0])]
            self.isHappy = 0
            self.isAsleep = 0
            self.state = 0
            self.hasBeenMoving = 0
            self.pet_names = ["orange_cat","grey_cat","emelem_cat"]
            self.which_pet = 2
            self.dance() # start the adc loop

        
   
          
        

        def dance(self):
          
            
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
           
            self.thing+=1
            #print(self.state)
            cur_order= self.orders[self.state]
            cycle_len = cur_order[0] * len(cur_order[1])
            if self.state == 2 and self.thing ==cycle_len:
                self.state = 0
            self.thing %= cycle_len
            index = self.thing // cur_order[0]

            img_original = Image.open("images/"+self.pet_names[self.which_pet]+"/" + self.state_names[self.state]+"_"+str(cur_order[1][index])+".png")
            
            img_original = img_original.resize((150, 150), Image.ANTIALIAS)
            
            # print(self.info.isMoviang)aa
            # plt.imshow(ImageGrab.grab(a))a
            # plt.show()
            img = ImageTk.PhotoImage(img_original)
            lbl = tk.Label(self, image = img)
            lbl.image = img
            lbl.grid(row=0, column = 0, columnspan = 1)
            def beHappy(event):
                print ("clicked at", event.x, event.y)
                #self.isHappy = 1
                if (self.info.isMoving==0):
                    self.state = 2
                    self.thing = -1
                    def play_sound():
                        playsound("images/"+self.pet_names[self.which_pet]+"/meow.mp3")
                    thread = Thread(target=play_sound)
                    thread.start()
            
            def beSleep(event):
                print ("clicked at", event.x, event.y)
                #self.isHappy = 1a
                print(event.char)
                if (self.info.isMoving==0):
                    self.state = 3
                    self.thing = -1
                    def play_sound():
                        playsound("images/"+self.pet_names[self.which_pet]+"/purr.mp3")
                    thread = Thread(target=play_sound)
                    thread.start()
            def beStill(event):
                print ("clicked at", event.x, event.y)
                if (self.info.isMoving==0):
                    self.state = 4
                    self.thing = -1
            def changeCat(event):
                self.which_pet += 1
                self.which_pet %= len(self.pet_names)


            # frame = tk.Frame(root, width=100, height=100)aa
            lbl.bind("<Button-1>", beHappy)
            lbl.bind("<Shift-Button-1>", beSleep)
            lbl.bind("<Control-Button-1>", beStill)
            lbl.bind("<Shift-Control-Button-1>", changeCat)
        
            self.after(100, self.dance) # ask the mainloop to call this metahod again in 1,000 milliseconds

        

        





    root =tk.Tk()

    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    # root.geometry(str(150)+"x"+str(150))

    root.title('PETSCREEN')

    view = PetScreen(root,info)
    root.resizable(False,False)
    # frame = tk.Frame(root)


    root.mainloop()

    # root = tk.Tk()

    # def callback(event):
    #     print ("clicked at", event.x, event.y)

    # frame = tk.Frame(root, width=100, height=100)
    # frame.bind("<Button-1>", callback)
    # frame.pack()

    # root.mainloop()
   



    

start_time = perf_counter()

# create two new threads
stuff = UsefulInfo()
t1 = Thread(target=lambda:ahkScreenMover(stuff))
t2 = Thread(target=lambda:runPetScreen(stuff))

t2.start()
t1.start()


# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')