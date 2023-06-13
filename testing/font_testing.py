import pyglet,tkinter
pyglet.font.add_file('VT323-Regular.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root,text="test",font=("VT323-Regular",25))
MyLabel.pack()
root.mainloop()