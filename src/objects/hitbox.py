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
        # Rectangle
        self.scale = 0.25
        self.hitbox = shapes.Rectangle(x_pos, y_pos, width, height, color=color, batch=self.background)

    def draw(self, x, y):
        self.hitbox_rect = shapes.Rectangle(x, y, self.width, self.height, color=self.color, batch=self.background)
        self.hitbox_rect.draw()

    def adjust_hitbox_position(self, enemy, hitbox, index, diff):
        if hitbox.y_pos <= 0:
            self.hitboxes.pop(index)
        else:
            hitbox.draw(enemy.x_pos + diff, enemy.y_pos + diff)