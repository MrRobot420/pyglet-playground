from datetime import datetime as dtime
from pyglet import sprite

from handler.resource_handler import ResourceHandler


class Bullet:
    def __init__(self, x, y, target_x, target_y, background):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.target_x = target_x
        self.target_y = target_y
        self.scale = 0.0625
        self.background = background
        self.start_time = dtime.now().timestamp()

        self.resource_handler = ResourceHandler()
        self.bullet_image = self.resource_handler.return_bullet()

        self.bullet_sprite = sprite.Sprite(self.bullet_image, self.x, self.y, batch=self.background)
        self.bullet_sprite.scale = self.scale
        self.image_width = self.bullet_image.width * self.scale
        self.image_height = self.bullet_image.height * self.scale

    
    def draw(self):
        self.bullet_sprite = sprite.Sprite(self.bullet_image, self.x, self.y, batch=self.background)
        # turn bullet
        self.bullet_sprite.scale = self.scale


    def update_bullet(self, x, y):
        self.x = x
        self.y = y
        self.draw()
    