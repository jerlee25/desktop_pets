import pyglet

pyglet.font.add_file('VT323-Regular.ttf')
window = pyglet.window.Window()
label = pyglet.text.Label('LAUNCH',
                          font_name='VT323',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
# button = pyglet.gui.PushButton(0, 0, pyglet.image.AbstractImage(), pyglet.image.AbstractImage(), hover=None)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()