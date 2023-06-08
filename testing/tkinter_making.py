import tkinter as tk 
from PIL import ImageGrab
from PIL import Image
from PIL import ImageTk
from ahk import AHK

import matplotlib.pyplot as plt



ahk = AHK()

# Tasks to do:
# X Create a Model object to maintain data and handle business logic
# - Implement functions that connect User Events 
#   to behaviors of the Model, and update the GUI
#   based on the results
# After the model
# - Improve the GUI separate from the model: add images to the buttons
# - Improve the Model separate from the GUI: make computer "smart" (see rps_model_v2.py) 
root = tk.Tk()
SCREENW =  1504
SCREENH =  1003


class RPS_Application(tk.Frame):

    def __init__(self, master):

        super().__init__(master)
        self.grid()
      

        self.create_widgets()
    
    def create_widgets(self):
        # c = tk.Canvas(self,bg="blue",width=SCREENW,height=SCREENW)
        # c.grid(row=0, column = 0, columnspan = 1)
       

        px = ImageGrab.grab().load()
        img_original = ImageGrab.grab()
        print(type(img_original))
        img_original = img_original.resize((int(SCREENW), SCREENH), Image.ANTIALIAS)
        
        # plt.imshow(ImageGrab.grab())
        # plt.show()
        img = ImageTk.PhotoImage(img_original)
        lbl = tk.Label(self, image = img)
        lbl.image = img
        lbl.grid(row=0, column = 0, columnspan = 1)
                
        # for x in range(0,int(SCREENW),1):
        #     for y in range(0,int(SCREENH),1):
        #         # pixelcolor = ahk.pixel_get_color(x,y)
        #         # print(pixelcolor)
        #         color = px[x, y]
                
                
        #         pixelcolor = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        #         # print(color)
        #         # print(pixelcolor)
        #         #pixelcolor = "#"+pixelcolor[2:]
                
        #         # pixelcolor ="green"
                
        #         c.create_line(x, y, x + 1, y,fill=pixelcolor)
       

     

    

    def reset_game(self):
        pass




screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(int(screen_width/2))+"x"+str(screen_height))
print(screen_width,screen_height)
root.title('RPS (starter)')
view = RPS_Application(root)
root.mainloop()
   