import pyglet.sprite
from pyglet import shapes, sprite

class Hitbox:
    def __init__(self, speed, width, height, x_pos, y_pos, background, color):
        self.speed = speed
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.background = background
        self.color = color
        # Png
        self.scale = 0.25
        self.hitbox = shapes.Rectangle(x_pos, y_pos, width, height, color=color, batch=self.background)

    def draw(self, x, y):
        self.hitbox_rect = shapes.Rectangle(x, y, self.width, self.height, color=self.color, batch=self.background)
        # self.hitbox_sprite = pyglet.sprite.Sprite(self.hitbox, x, y, batch=self.background)
        self.hitbox_rect.draw()

    def update(self, dt):
        self.y_pos -= self.speed * dt