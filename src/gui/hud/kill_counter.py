import pyglet
from gui.elements.label import Label

class KillCounter(pyglet.text.Label):
    def __init__(self, enemy_count, x, y, color=(55, 160, 55, 255), font_name='Evil Empire'):
        super().__init__()
        self.enemy_amount = enemy_count
        self.x = x
        self.y = y
        self.color = color
        self.font_name = font_name
        self.killed = 0
        self.counter = Label(f'({self.killed}/{self.enemy_amount})', self.x, self.y, self.color, 36, font_name)

    def draw(self):
        self.counter = Label(f'({self.killed}/{self.enemy_amount})', self.x, self.y, self.color, 36, self.font_name)
        self.counter.draw()

    def update_counter(self):
        self.killed += 1
        self.counter.draw()
    
    def reset_counter(self, new_enemy_count):
        self.killed = 0
        self.enemy_amount = new_enemy_count

    def update_enemy_amount(self, amount):
        self.enemy_amount += amount