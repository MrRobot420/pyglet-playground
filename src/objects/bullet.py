from pyglet import sprite

from handler.resource_handler import ResourceHandler


class Bullet:
    def __init__(self, x, y, background):
        self.x = x
        self.y = y
        self.scale = 0.25
        self.background = background

        self.resource_handler = ResourceHandler()
        self.bullet_image = self.resource_handler.return_bullet()

        self.bullet_sprite = sprite.Sprite(self.bullet_image, self.x, self.y, batch=self.background)
        self.bullet_sprite.scale = self.scale
        self.image_width = self.bullet_image.width * self.scale
        self.image_height = self.bullet_image.height * self.scale

    
    def draw(self):
        self.bullet.draw()
        self.bullet_sprite = sprite.Sprite(self.bullet_image, self.x, self.y, batch=self.background)
        self.bullet_sprite.scale = self.scale


    def update_bullet(self):
        pass
    