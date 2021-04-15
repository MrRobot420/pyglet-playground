import pyglet
from pyglet.gl import *

from gui.cursor import Cursor
from gui.hud import HUD
from handler.enemy_handler import EnemyHandler

key = pyglet.window.key


class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)
        self.background = pyglet.graphics.Batch()
        self.x, self.y = 0, 0
        
        self.cursor = Cursor(self.background)
        self.enemy_handler = EnemyHandler(self.width, self.height, self.background)
        self.hud = HUD(self.width, self.height, len(self.enemy_handler.enemies))

        self.keys = {}
        self.mouse_x = 0
        self.mouse_y = 0
        self.alive = 1
        self.enemies = []

    
    def on_draw(self):
        dt = pyglet.clock.tick()
        self.render(dt)
    

    def on_close(self):
        self.enemies = []
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
        if symbol == key.ESCAPE:  # [ESC]
            self.enemies = []
            self.alive = 0

        self.keys[symbol] = True


    def render(self, dt):
        self.clear()
        self.enemy_handler.handle_enemies(self.mouse_x, self.mouse_y, self.hud, dt)

        self.hud.draw()
        self.cursor.draw(self.mouse_x, self.mouse_y)
        self.flip()

    def update(self, dt):
        while self.alive == 1:
            self.render(dt)
            self.dispatch_events()
        self.close()
