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
        self.resume_button = Button(self.button_width, self.button_height, self.x, self.y, 12, 5, 'R E S U M E', (1, 1, 1), (60, 235, 50, 255))
        self.start_button = Button(self.button_width, self.button_height, self.x, self.y - 80, 6, 5, 'S T A R T', (1, 1, 1), (60, 235, 50, 255))

    def draw(self):
        self.start_button.draw()
        self.resume_button.draw()

    
    def button_was_clicked(self, x, y, button):
        if (x >= int(button.x)) and (x <= int(button.x) + (self.button_width)):
            if (y >= int(button.y)) and (y <= int(button.y) + (self.button_height)):
                return True
        return False