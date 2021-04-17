
from gui.elements.label import Label

class LevelInfo:
    def __init__(self, x, y, color):
        self.current_level = 0
        self.x = x
        self.y = y
        self.color = color
        self.level_label = Label(f'Level: {self.current_level + 1}', x, y, color)

    def draw(self):
        self.level_label.draw()
    
    def update_level(self):
        self.current_level += 1
        self.level_label = Label(f'Level: {self.current_level + 1}', self.x, self.y, self.color)

    def reset_level(self):
        self.current_level = 0
        self.level_label = Label(f'Level: {self.current_level + 1}', self.x, self.y, self.color)