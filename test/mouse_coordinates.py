import time
import pyglet
from pyglet.window import mouse
from pyglet.gl import *
from cursor import Cursor

key = pyglet.window.key

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)
        pyglet.gl.glClearColor(0.9,0.9,0.9,1)
        self.background = pyglet.graphics.Batch()
        self.cursor = Cursor(self.background)

        self.x, self.y = 0, 0

        self.keys = {}

        self.mouse_x = 0
        self.mouse_y = 0

        self.alive = 1


    def on_draw(self):
        self.render()
    
    def on_close(self):
        self.alive = 0
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_key_release(self, symbol, modifiers):
        try:
            del self.keys[symbol]
        except:
            pass

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE: # [ESC]
            self.alive = 0

        self.keys[symbol] = True

    def render(self):
        self.clear()
        self.cursor.draw(self.mouse_x, self.mouse_y)

        self.flip()
    
    def run(self):
        while self.alive == 1:
            self.render()
            event = self.dispatch_events()

    
if __name__ == '__main__':
    # pyglet.clock.schedule_interval(update, 1 / 120.0)
    game_window = MainWindow(1280, 960, 'Game Name', resizable=True)
    game_window.set_mouse_visible(False) # Hide the mouse cursor
    game_window.run()