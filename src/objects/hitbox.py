import pyglet.sprite
from pyglet import shapes, sprite


class Hitbox:
    def __init__(self, speed, size, x_pos, y_pos, background):
        self.speed = speed
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.background = background
        # Png
        self.scale = 0.25
        self.hitbox = shapes.Rectangle(200, 200, 100, 200, color=(55, 55, 255), batch=self.background)
        self.cursor_sprite = sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width * self.scale
        self.image_height = self.image.height * self.scale

    def draw(self, x, y):
        self.hitbox_sprite = pyglet.sprite.Sprite(self.image, x, y, batch=self.background)
        self.hitbox_sprite.draw()

    def update(self, dt):
        self.y_pos -= self.speed * dt
