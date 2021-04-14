import pyglet
from .label import Label

class KillCounter(pyglet.text.Label):
    def __init__(self, enemy_count, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_amount = enemy_count
        self.killed = 0

    def draw(self):
        self.counter = Label(f'({self.killed}/{self.enemy_amount})', self.x, self.y, (55, 160, 55, 255))
        self.counter.draw()

    def update_counter(self):
        self.killed += 1
        self.counter.draw()
    
    def reset_counter(self, new_enemy_count):
        self.killed = 0
        self.enemy_amount = new_enemy_count