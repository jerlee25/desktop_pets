
from ahk import AHK

ahk = AHK()
print(ahk.mouse_position)
ahk.mouse_move(x=100, y=100, blocking=True)  # Blocks until mouse finishes moving (the default)
ahk.mouse_move(x=950, y=950, speed=10, blocking=True) # Moves the mouse to x, y taking 'speed' seconds to move
ahk.mouse_move(x=2008, y=97, speed=10, blocking=True)
ahk.click()
print(ahk.mouse_position)  #  (150, 150)
print(ahk.pixel_get_color(0,0))

#boop

# for window in ahk.list_windows():
#     print(window.title)