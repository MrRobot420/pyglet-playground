import random

import pyglet.sprite
from pyglet import shapes, clock, image, sprite


class Enemy:
    def __init__(self, speed, health, size, x_pos, y_pos, background):
        self.speed = speed
        self.health = health
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.background = background
        self.clock = clock
        # Png
        self.image = image.load('./resources/enemies/axolotl.png')
        self.cursor_sprite = sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width
        self.image_height = self.image.height

    def draw(self, x, y):
        scale = 0.25
        width = (self.image_width * scale) / 2
        height = (self.image_height * scale) / 2
        self.enemie_sprite = pyglet.sprite.Sprite(self.image, x - width, y - height, batch=self.background)
        # square = shapes.Rectangle(x, y, self.size, self.size, color=(55, 55, 2), batch=self.background)
        # square.draw()
        self.enemie_sprite.scale = scale
        self.enemie_sprite.draw()
        pass

    def update(self):
        print(f"Enemy last update: {self.clock.tick()}")
        self.y_pos -= self.speed * 1000 * self.clock.tick()
