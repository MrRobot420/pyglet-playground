from gui.elements.label import Label
from pyglet.shapes import Rectangle

class Button:
    def __init__(self, width, height, x, y, x_shift, y_shift, text, color, font_color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font_color = font_color
        self.x_shift = width / x_shift
        self.y_shift = height / y_shift

    def draw(self):
        self.rect = Rectangle(self.x, self.y, self.width, self.height, self.color)
        self.rect.draw()
        self.description = Label(self.text, self.x + self.x_shift, self.y + self.y_shift, self.font_color)
        self.description.draw()