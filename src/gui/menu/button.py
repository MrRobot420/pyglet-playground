from gui.elements.label import Label
from pyglet.shapes import Rectangle

class Button:
    def __init__(self, width, height, x, y, x_shift, y_shift, text, color, font_color):
        self.x = x
        self.y = y
        self.rect = Rectangle(x, y, width, height, color)
        self.description = Label(text, x + x_shift, y + y_shift, font_color)

    def draw(self):
        self.rect.draw()
        self.description.draw()