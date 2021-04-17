import pyglet.sprite
from pyglet import image, sprite


class Enemy:
    def __init__(self, speed, health, x_pos, y_pos, background, enemy_type):
        self.speed = speed
        self.health = health
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.background = background
        # Png
        self.scale = 0.25
        self.image = image.load(f'./resources/enemies/{enemy_type}.png')
        self.cursor_sprite = sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width * self.scale
        self.image_height = self.image.height * self.scale

    def draw(self, x, y):
        self.enemy_sprite = pyglet.sprite.Sprite(self.image, x, y, batch=self.background)
        self.enemy_sprite.scale = self.scale

    def update(self, dt):
        self.y_pos -= self.speed * dt
