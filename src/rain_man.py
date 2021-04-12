import pyglet
from pyglet.gl import *

from gui.cursor import Cursor
from gui.label import Label
from gui.score import ScoreLabel
from handler.enemy_handler import EnemyHandler

key = pyglet.window.key


class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)
        self.background = pyglet.graphics.Batch()
        self.cursor = Cursor(self.background)
        self.x, self.y = 0, 0
        self.cursor_info = Label(f'x: {self.x}, y: {self.y}', self.width - 50, self.height - 36)
        self.enemies = []
        self.score = ScoreLabel(0 + 5, self.height - 40)
        self.enemy_handler = EnemyHandler(self.width, self.height, self.background)

        self.keys = {}
        self.mouse_x = 0
        self.mouse_y = 0

        self.alive = 1

    
    def on_draw(self):
        dt = pyglet.clock.tick()
        self.render(dt)
    

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
        if symbol == key.ESCAPE:  # [ESC]
            self.alive = 0

        self.keys[symbol] = True


    def render(self, dt):
        self.clear()
        self.enemy_handler.handle_enemies(self.mouse_x, self.mouse_y, self.score)

        self.score.draw()
        self.cursor.draw(self.mouse_x, self.mouse_y)
        self.cursor_info = Label(f'x: {self.mouse_x}, y: {self.mouse_y}', self.width - 310, self.height - 36)
        self.cursor_info.draw()
        self.flip()

    def update(self, dt):
        while self.alive == 1:
            self.render(dt)
            self.dispatch_events()
        self.close()


if __name__ == '__main__':
    game_window = MainWindow(1280, 960, 'Game Name', resizable=True)
    pyglet.clock.schedule_interval(game_window.update, 1/60.0)
    game_window.set_mouse_visible(False)  # Hide the mouse cursor
    pyglet.app.run()
