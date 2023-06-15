import tkinter as tk
import tkinter.ttk as ttk
import pyglet

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widget()
    
    def create_widget(self):

        style = ttk.Style()
        pyglet.font.add_file('VT323-Regular.ttf')
        style.configure("TButton", font = ('VT323', 30, 'bold'), foreground = 'red')
        style.map("TButton", foreground = [('active', '!disabled', 'red')],
                     background = [('active', 'grey')])
        button = ttk.Button(self, text = "Launch!", style = "TButton", command = root.destroy).grid(
                            row = 0, column = 0, padx = 100, pady = 100)
        
        # uploading images option
        # customizing menu
    
    
root = tk.Tk()
root.title("A Window!")
root.geometry("500x500")
app = Application(root)

root.mainloop()
