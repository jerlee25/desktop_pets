import tkinter as tk
from tkextrafont import Font

window = tk.Tk()
font = Font(file="tests/overhaul.ttf", family="Overhaul")
tk.Label(window, text="Hello", font=font).pack()
window.mainloop()