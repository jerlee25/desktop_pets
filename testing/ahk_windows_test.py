from ahk import AHK

ahk = AHK()

ahk.run_script('Run Notepad') # Open notepad

win = ahk.find_window(title='Untitled - Notepad') # Find the opened window
win.always_on_top = 'On'
win.set_always_on_top('On')
print(win)
win.move(x=200, y=300, width=1, height=1)

