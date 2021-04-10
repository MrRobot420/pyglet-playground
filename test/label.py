import pyglet

class Label(pyglet.text.Label):
    def __init__(self, text, x, y):
        super().__init__()
        self.text = text
        self.label = pyglet.text.Label(text, x=x, y=y, font_name='Times New Roman', font_size=36, color=(1, 1, 1, 255))

    def draw(self):
        self.label.draw()