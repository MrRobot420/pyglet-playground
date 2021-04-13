import pyglet

class Cursor():
    def __init__(self, background):
        self.background = background
        self.image = pyglet.image.load('./resources/cursor/red_cross.png')
        self.cursor_sprite = pyglet.sprite.Sprite(self.image, 0, 0)
        self.image_width = self.image.width
        self.image_height = self.image.height
        self.was_clicked = False
        self.x = 0
        self.y = 0

    
    def draw(self, mouse_x, mouse_y):
        '''draw the cursor at the x and y position of the mouse'''
        scale = 0.07
        width = (self.image_width * scale) / 2
        height = (self.image_height * scale) / 2
        self.x = mouse_x + width
        self.y = mouse_y + height
        self.cursor_sprite = pyglet.sprite.Sprite(self.image, self.x - (width*2), self.y - (height*2), batch=self.background)
        self.cursor_sprite.scale = scale
        self.cursor_sprite.draw()