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
        self.image_width = 64
        self.image_height = 64

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
        # self.image.blit(x, y, z=0, width=self.image_width, height=self.image_height)

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

        ## Add stuff you want to render here.
        ## Preferably in the form of a batch.
        self.image.blit(self.mouse_x-self.image_width/2, self.mouse_y-self.image_height/2, z=0, width=self.image_width, height=self.image_height)

        self.flip()
    
    def run(self):
        while self.alive == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()

    
if __name__ == '__main__':
    # pyglet.clock.schedule_interval(update, 1 / 120.0)
    game_window = MainWindow(1280, 960, 'Game Name', resizable=True)
    game_window.run()