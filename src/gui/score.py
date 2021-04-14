import pyglet

class ScoreLabel(pyglet.text.Label):
    def __init__(self, x, y):
        super().__init__()
        self.value = 0
        self.x = x
        self.y = y
        self.text = f'Score: {self.value}'

    def draw(self):
        self.label = pyglet.text.Label(self.text, x=self.x, y=self.y, font_name='Times New Roman', font_size=36, color=(55, 160, 55, 255))
        self.label.draw()

    def updateScore(self, points=10):
        self.value += points
        self.text = f'Score: {self.value}'
        self.draw()
