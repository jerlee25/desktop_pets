import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widget()
    
    def create_widget(self):
        tk.Label(self, text = "").grid(row = 0, column = 0, sticky = tk.W)
        tk.Label(self, text = "").grid(row = 1, column = 0, sticky = tk.W)
        tk.Label(self, text = "").grid(row = 0, column = 1, sticky = tk.W)
        tk.Label(self, text = "").grid(row = 1, column = 1, sticky = tk.W)
        button = tk.Button(self, text = "Launch!", ).grid(row = 2, column = 2)
        
        # uploading images option
        # customizing menu
    
root = tk.Tk()
root.title("A Window!")
root.geometry("500x500")
app = Application(root)

root.mainloop()