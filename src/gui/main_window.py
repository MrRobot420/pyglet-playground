import pyglet
from pyglet.gl import *

from gui.elements.cursor import Cursor
from gui.hud.hud import HUD
from handler.enemy_handler import EnemyHandler

key = pyglet.window.key


class MainWindow(pyglet.window.Window):
    def __init__(self, cursor, enemy_handler, hud, *args, **kwrgs, ):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)
        self.x, self.y = 0, 0
        
        self.cursor = cursor
        self.enemy_handler = enemy_handler
        self.hud = hud

        self.keys = {}
        self.mouse_x = 0
        self.mouse_y = 0
        self.alive = 1

    
    def on_draw(self):
        dt = pyglet.clock.tick()
        self.render(dt)
    

    def on_close(self):
        self.enemy_handler.enemies = []
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
            self.enemy_handler.enemies = []
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
