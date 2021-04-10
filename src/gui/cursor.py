import pyglet


class Cursor:
    def __init__(self, background):
        self.background = background
        self.image = pyglet.image.load('./resources/cursor/red_cross.png')
        self.cursor_sprite = pyglet.sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width
        self.image_height = self.image.height

    def draw(self, mouse_x, mouse_y):
        '''draw the cursor at the x and y position of the mouse'''
        scale = 0.07
        width = (self.image_width * scale) / 2
        height = (self.image_height * scale) / 2
        self.cursor_sprite = pyglet.sprite.Sprite(self.image, mouse_x - width, mouse_y - height, batch=self.background)
        self.cursor_sprite.scale = scale
        self.cursor_sprite.draw()

    def fire(self, x, y):
        self.x_cursor = x
        self.y_cursor = y
