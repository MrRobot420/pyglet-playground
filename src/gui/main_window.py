import pyglet
from pyglet.gl import *

from handler.event_handler import GameEventHandler

class MainWindow(pyglet.window.Window):
    def __init__(self, cursor, enemy_handler, hud, pause_menu, *args, **kwrgs):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)
        self.cursor = cursor
        self.enemy_handler = enemy_handler
        self.hud = hud
        self.pause_menu = pause_menu
        self.menu_visible = True

        self.mouse_x = 0
        self.mouse_y = 0

        self.game_event_handler = GameEventHandler(self.update_mouse_coordinates)
        self.push_handlers(self.game_event_handler)


    def update_mouse_coordinates(self, x, y):
        self.mouse_x = x
        self.mouse_y = y


    def on_draw(self):
        dt = pyglet.clock.tick()
        self.render(dt)


    def render(self, dt):
        self.clear()

        if not self.menu_visible:
            self.set_mouse_visible(False)
            self.enemy_handler.handle_enemies(self.mouse_x, self.mouse_y, self.hud, dt)

            self.hud.draw()
            self.cursor.draw(self.mouse_x, self.mouse_y)
        else:
            self.pause_menu.draw()
            self.set_mouse_visible(True)

        self.flip()


    def update(self, dt):
        while self.game_event_handler.alive == 1:
            self.render(dt)
            self.dispatch_events()
        self.close()