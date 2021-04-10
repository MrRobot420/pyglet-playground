import pyglet

class ScoreLabel(pyglet.text.Label):
    def __init__(self, text, x, y):
        super().__init__()
        self.text = text

    def draw(self):
        self.label = pyglet.text.Label(self.text, x=x, y=y, font_name='Times New Roman', font_size=36, color=(1, 1, 1, 255))
        self.label.draw()

    def updateScore(self):
        pass
