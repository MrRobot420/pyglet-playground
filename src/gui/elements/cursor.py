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
        self.scale = 0.07
        self.width = (self.image_width * self.scale) / 2
        self.height = (self.image_height * self.scale) / 2

    
    def draw(self, mouse_x, mouse_y):
        '''draw the cursor at the x and y position of the mouse'''
        self.x = mouse_x + self.width
        self.y = mouse_y + self.height
        self.cursor_sprite = pyglet.sprite.Sprite(self.image, self.x - (self.width*2), self.y - (self.height*2), batch=self.background)
        self.cursor_sprite.scale = self.scale