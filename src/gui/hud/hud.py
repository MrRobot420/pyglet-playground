from .score import ScoreLabel
from .kill_counter import KillCounter

class HUD:
    def __init__(self, width, height, enemy_count, color=(55, 160, 55, 255)):
        self.width = width
        self.height = height
        
        self.score = ScoreLabel(0 + 5, self.height - 40, color)
        self.kill_count = KillCounter(enemy_count, self.width - 200, self.height - 40, color)

    def draw(self):
        self.score.draw()
        self.kill_count.draw()

    def update(self):
        self.score.updateScore()
        self.kill_count.update_counter()