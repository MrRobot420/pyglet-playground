from .label import Label
from .score import ScoreLabel

class HUD:
    def __init__(self, width, height):
        self.width = width,
        self.height = height
        self.score = ScoreLabel(0 + 5, self.height - 40)
        pass

    def draw(self):
        self.score.draw()