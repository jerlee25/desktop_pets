import tkinter as tk
from tkextrafont import Font

window = tk.Tk()
font = Font(file="testing/VT323-Regular.ttf", family="VT323")
tk.Label(window, text="Hello", font=font).pack()
window.mainloop()