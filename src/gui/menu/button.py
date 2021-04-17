from gui.elements.label import Label
from pyglet.shapes import Rectangle

class Button:
    def __init__(self, width, height, x, y, x_shift, y_shift, text, color, font_color):
        self.x = x
        self.y = y
        self.rect = Rectangle(x, y, width, height, color)
        self.x_shift = width / x_shift
        self.y_shift = height / y_shift
        self.description = Label(text, x + self.x_shift, y + self.y_shift, font_color)

    def draw(self):
        self.rect.draw()
        self.description.draw()