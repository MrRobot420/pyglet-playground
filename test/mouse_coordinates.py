import time
import pyglet
from pyglet.window import mouse
from pyglet.gl import *

key = pyglet.window.key

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)
        pyglet.gl.glClearColor(0.9,0.9,0.9,1)
        self.image = pyglet.image.load('./resources/cursor/red_cross.png')
        self.background = pyglet.graphics.Batch()
        self.cursor = pyglet.sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width
        self.image_height = self.image.height

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
        scale = 0.07
        width = (self.image_width * scale) / 2
        height = (self.image_height * scale) / 2
        self.cursor = pyglet.sprite.Sprite(self.image, self.mouse_x-width, self.mouse_y-height, batch=self.background)
        self.cursor.scale = scale
        self.cursor.draw()

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