from gui.elements.label import Label
from pyglet.shapes import Rectangle

class Button:
    def __init__(self, width, height, x, y, text, color, font_color):
        self.rect = Rectangle(x, y, width, height, color)
        self.description = Label(text, x + (width / 6), y + (height / 5), font_color)

    def draw(self):
        self.rect.draw()
        self.description.draw()