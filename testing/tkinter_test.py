#Import the required libraries
from tkinter import *


win= Tk()

#Set the geometry of frame
win.geometry("650x250")

#Get the current screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win.geometry(str(screen_width)+"x"+str(screen_height))

#Print the screen size
print("Screen width:", screen_width)
print("Screen height:", screen_height)


win.mainloop()

 
root = Tk()
root.geometry("200x150")
root.tk.call('tk', 'scaling', 2.0)
 
label = Label(root, text = "Hello World")
label.pack(padx = 5, pady = 5)
 
root.mainloop()