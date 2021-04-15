import pyglet

class Label(pyglet.text.Label):
    def __init__(self, text, x, y, color=(1, 1, 1, 255)):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.label = pyglet.text.Label(text, x=x, y=y, font_name='Times New Roman', font_size=36, color=color)

    def draw(self):
        self.label.draw()

    def update_text(self, text):
        self.text = text
        self.label = pyglet.text.Label(self.text, self.x, self.y, font_name='Times New Roman', font_size=36, color=(1, 1, 1, 255))