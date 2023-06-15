import tkinter as tk 
from PIL import ImageGrab
from PIL import Image
from PIL import ImageTk
from ahk import AHK
import random





ahk = AHK()

class PetScreen(tk.Frame):
  
    def __init__(self, master):

        super().__init__(master)
        self.grid()
        self.thing =  1

        self.create_widgets()
        self.dance() # start the adc loop

    
    def create_widgets(self):
        # c = tk.Canvas(self,bg="blue",width=SCREENW,height=SCREENW)
        # c.grid(row=0, column = 0, columnspan = 1)
       
        
        px = ImageGrab.grab().load()
        img_original = Image.open("images/smiley.jpg")
        print(type(img_original))
        img_original = img_original.resize((150, 150), Image.ANTIALIAS)
        
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
       

    def dance(self):
        self.thing+=1
       
        self.thing %=11
        img_original = Image.open("images/flames/flame"+str(self.thing)+".gif")
        
        img_original = img_original.resize((150, 150), Image.ANTIALIAS)
        
        # plt.imshow(ImageGrab.grab())
        # plt.show()
        img = ImageTk.PhotoImage(img_original)
        lbl = tk.Label(self, image = img)
        lbl.image = img
        lbl.grid(row=0, column = 0, columnspan = 1)
       
        self.after(100, self.dance) # ask the mainloop to call this method again in 1,000 milliseconds

    

    


root =tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(150)+"x"+str(150))

root.title('PETSCREEN')
root.resizable(False,False)
view = PetScreen(root)
root.mainloop()
   


