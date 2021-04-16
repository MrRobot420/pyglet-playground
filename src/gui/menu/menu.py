import pyglet

from gui.menu.button import Button

class Menu:
    def __init__(self, window_width, window_height):
        # TODO: pass game_event_handler?
        self.win_width = window_width
        self.win_height = window_height
        self.button_width = 300
        self.button_height = 50
        self.x = (self.win_width / 2) - (self.button_width / 2)
        self.y = (self.win_height / 2) - (self.button_height / 2)
        self.start_button = Button(self.button_width, self.button_height, self.x, self.y, 'S T A R T', (1, 1, 1), (60, 235, 50, 255))

    def draw(self):
        self.start_button.draw()