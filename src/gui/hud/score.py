import pyglet

class ScoreLabel(pyglet.text.Label):
    def __init__(self, x, y, color=(55, 160, 55, 255)):
        super().__init__()
        self.value = 0
        self.x = x
        self.y = y
        self.color = color
        self.text = f'Score: {self.value}'

    def draw(self):
        self.label = pyglet.text.Label(self.text, x=self.x, y=self.y, font_name='Times New Roman', font_size=36, color=self.color)
        self.label.draw()

    def updateScore(self, points=10):
        self.value += points
        self.text = f'Score: {self.value}'
        self.draw()

    def reset_score(self):
        self.value = 0
        self.text = f'Score: {self.value}'
        self.draw()