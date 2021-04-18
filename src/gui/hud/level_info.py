
from gui.elements.label import Label

class LevelInfo:
    def __init__(self, x, y, color, font_name='Evil Empire'):
        self.current_level = 0
        self.x = x
        self.y = y
        self.color = color
        self.font_name = font_name
        self.level_label = Label(f'Level: {self.current_level + 1}', x, y, color, 36, font_name)

    def draw(self):
        self.level_label.draw()
    
    def update_level(self):
        self.current_level += 1
        self.level_label = Label(f'Level: {self.current_level + 1}', self.x, self.y, self.color, 36, self.font_name)

    def reset_level(self):
        self.current_level = 0
        self.level_label = Label(f'Level: {self.current_level + 1}', self.x, self.y, self.color, 36, self.font_name)