

from pyglet import sprite
from handler.resource_handler import ResourceHandler


class Player:
    def __init__(self, x, y, background):
        self.x = x
        self.y = y
        self.background = background
        self.scale = 0.25
        self.resource_handler = ResourceHandler()
        self.image = self.resource_handler.return_player()
        self.player_sprite = sprite.Sprite(self.image, self.x, self.y, batch=self.background)
        self.player_sprite.scale = self.scale
        self.image_width = self.image.width * self.scale
        self.image_height = self.image.height * self.scale

    def draw(self, x, y):
        self.x = x
        self.y = y
        self.player_sprite = sprite.Sprite(self.image, self.x, self.y, batch=self.background)
        self.player_sprite.scale = self.scale

    # Maybe put it into the bullet /weapon class?
    def shoot(self):
        self.bullet = self.resource_handler.return_bullet()