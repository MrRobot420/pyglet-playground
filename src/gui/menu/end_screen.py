from pyglet.shapes import Rectangle

from gui.elements.button import Button
from gui.elements.label import Label

class EndScreen:
    def __init__(self, window_width, window_height, score, kill_count, total_enemies):
        self.win_width = window_width
        self.win_height = window_height
        self.score = score
        self.kill_count = kill_count
        self.button_width = 300
        self.button_height = 50
        self.x = (self.win_width / 2) - (self.button_width / 2)
        self.y = (self.win_height / 2) - (self.button_height / 2)
        self.pop_up = Rectangle(self.x - 100, self.y - 300, 500, 800, (50, 50, 50))
        self.title = Label('G A M E   O V E R!', self.x + 5, self.y + 90, (150, 1, 1, 255))
        self.info_label_score = Label(f'SCORE: {self.score}', self.x + 50, self.y, (60, 135, 50, 255))
        self.info_label_kills = Label(f'KILLS: {self.kill_count} / {total_enemies}', self.x + 15, self.y - 50, (60, 135, 50, 255))
        self.menu_button = Button(self.button_width, self.button_height, self.x, self.y - 150, 3.4, 5, 'M E N U', (1, 1, 1), (60, 235, 50, 255))

    def draw(self):
        self.pop_up.draw()
        self.info_label_score.draw()
        self.info_label_kills.draw()
        self.menu_button.draw()
        self.title.draw()

    def button_was_clicked(self, x, y, button):
        if (x >= int(button.x)) and (x <= int(button.x) + (self.button_width)):
            if (y >= int(button.y)) and (y <= int(button.y) + (self.button_height)):
                return True
        return False

    def button_was_touched(self, x, y, button):
        if (x >= int(button.x)) and (x <= int(button.x) + (self.button_width)):
            if (y >= int(button.y)) and (y <= int(button.y) + (self.button_height)):
                return True
        return False