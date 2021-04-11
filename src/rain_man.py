import pyglet
from pyglet import clock
from pyglet.gl import *
import random

from gui.cursor import Cursor
from gui.label import Label
from gui.score import ScoreLabel
from objects.enemy import Enemy

key = pyglet.window.key


class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)
        self.background = pyglet.graphics.Batch()
        self.cursor = Cursor(self.background)
        self.clock = clock
        self.x, self.y = 0, 0
        self.cursor_info = Label(f'x: {self.x}, y: {self.y}', self.width - 50, self.height - 36)
        self.enemies = []
        self.score = ScoreLabel(0 + 5, self.height - 40)
        for index in range(10):
            self.enemies.append(Enemy(random.randint(100, 300),
                                      100,
                                      random.randint(5, 30),
                                      random.randint(1, self.width),
                                      self.height,
                                      self.background))

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
        if symbol == key.ESCAPE:  # [ESC]
            self.alive = 0

        if symbol == key.SPACE:
            self.cursor.fire()

        self.keys[symbol] = True

    def render(self):
        self.clear()

        for index, enemy in enumerate(self.enemies):
            if enemy.y_pos <= 0:
                self.enemies.pop(index)
                self.enemies.append(
                    Enemy(random.randint(100, 300),
                          100,
                          random.randint(5, 30),
                          random.randint(1, self.width),
                          self.height,
                          self.background)
                )
                
            enemy.draw(enemy.x_pos, enemy.y_pos)
            enemy.update()
            if (int(enemy.x_pos) >= self.mouse_x) & (int(enemy.x_pos) <= self.mouse_x + (enemy.image_width * enemy.scale)):
                # print('intersects with x axis of object')
                if (int(enemy.y_pos) >= int(self.mouse_y)) & (int(enemy.y_pos) <= self.mouse_y + (enemy.image_height * enemy.scale)):
                    # print('intersects with y axis of object')
                    self.enemies.pop(index)
                    self.score.updateScore()
                    # self.score.updateScore()
        self.score.draw()
        self.cursor.draw(self.mouse_x, self.mouse_y)
        self.cursor_info = Label(f'x: {self.mouse_x}, y: {self.mouse_y}', self.width - 310, self.height - 36)
        self.cursor_info.draw()
        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()
            event = self.dispatch_events()


if __name__ == '__main__':
    game_window = MainWindow(1280, 960, 'Game Name', resizable=True)
    game_window.set_mouse_visible(False)  # Hide the mouse cursor
    game_window.run()
