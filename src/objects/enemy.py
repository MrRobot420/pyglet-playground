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
        self.scale = 0.25
        self.image = image.load('./resources/enemies/axolotl.png')
        self.cursor_sprite = sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width * self.scale
        self.image_height = self.image.height * self.scale

    def draw(self, x, y):
        width = self.image_width / 2
        height = self.image_height / 2
        self.enemie_sprite = pyglet.sprite.Sprite(self.image, x - width, y - height, batch=self.background)
        self.enemie_sprite.scale = self.scale
        self.enemie_sprite.draw()
        pass

    def update(self, dt):
        self.y_pos -= self.speed * dt
