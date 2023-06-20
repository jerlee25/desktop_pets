import tkinter as tk
import tkinter.ttk as ttk
import pyglet
from PIL import Image, ImageTk
# from pet_screen import PetScreen

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widget()
    
    def create_widget(self):

        style = ttk.Style()
        pyglet.font.add_file('testing/VT323-Regular.ttf')
        style.configure("TButton", font = ('VT323', 30, 'bold'), foreground = 'red')
        style.map("TButton", foreground = [('active', '!disabled', 'red')],
                     background = [('active', 'grey')])
        button = ttk.Button(self, text = "Launch!", style = "TButton", command = self.open_pet).grid(
                            row = 0, column = 0, padx = 100, pady = 50)
        button2 = ttk.Button(self, text = "Customize!", style = "TButton", command = self.customize_pet).grid(
                            row = 1, column = 0, padx = 100, pady = 0)
        
        # uploading images option
        # customizing menu

    def open_pet(self):
        root.destroy()
        # pet = PetScreen()
        pass

    def customize_pet(self):
        # label = ttk.Label(self, image = ImageTk.PhotoImage(Image.open("images/emelem_cat/idle_0.png"))).grid(
        #                         row = 2, column = 0, padx = 75, pady = 25)
        # button.place_forget()
        img_original = Image.open("images/emelem_cat/idle_0.png")
        img_original = img_original.resize((root.winfo_width() - 275, root.winfo_height() - 275))
        img = ImageTk.PhotoImage(img_original)
        bg = tk.Label(root, image=img).grid(row = 2, column = 0, padx = 75, pady = 25)
        bg.image = img
        # bg.pack(side="bottom", fill="both", expand="yes")
    
root = tk.Tk()
root.title("A Window!")
root.geometry("500x500")

bg = tk.PhotoImage(file = "images/background.png")
# canvas1 = tk.Canvas(root, width = 400, height = 400)
# canvas1.pack(fill = "both", expand = True)
# canvas1.create_image(0, 0, image = bg, anchor = "nw")
label = tk.Label(root, image = bg)
label.place(x = 0,y = 0)

app = Application(root)

root.mainloop()
