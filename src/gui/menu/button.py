from gui.elements.label import Label
from pyglet.shapes import Rectangle

class Button:
    def __init__(self, width, height, x, y, x_shift, y_shift, text, color, font_color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.org_color = color
        self.org_font_color = font_color
        self.color = color
        self.font_color = font_color
        self.x_shift = width / x_shift
        self.y_shift = height / y_shift

    def draw(self):
        self.rect = Rectangle(self.x, self.y, self.width, self.height, self.color)
        self.rect.draw()
        self.description = Label(self.text, self.x + self.x_shift, self.y + self.y_shift, self.font_color)
        self.description.draw()

    def hovered(self):
        self.inverse_colors()
        self.draw()
    
    def not_hovered(self):
        self.color = self.org_color
        self.font_color = self.org_font_color
        self.draw()

    def inverse_colors(self):
        self.color = (self.org_font_color[0], self.org_font_color[1], self.org_font_color[2])
        self.font_color = (self.org_color[0], self.org_color[1], self.org_color[2], 255)