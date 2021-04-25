from pyglet.shapes import Rectangle

from gui.elements.button import Button
from gui.elements.label import Label

class Menu:
    def __init__(self, window_width, window_height):
        # TODO: pass game_event_handler?
        self.win_width = window_width
        self.win_height = window_height
        self.button_width = 300
        self.button_height = 50
        self.x = (self.win_width / 2) - (self.button_width / 2)
        self.y = (self.win_height / 2) - (self.button_height / 2)
        self.pop_up = Rectangle(self.x - 100, self.y - 300, 500, 800, (50, 50, 50))
        self.title = Label('M A I N   M E N U', self.x + 5, self.y + 120, (40, 110, 1, 255))
        self.start_button = Button(self.button_width, self.button_height, self.x, self.y, 3.7, 5, 'S T A R T', (1, 1, 1), (60, 235, 50, 255))
        self.resume_button = Button(self.button_width, self.button_height, self.x, self.y - 80, 5.4, 5, 'R E S U M E', (1, 1, 1), (60, 235, 50, 255))
        self.quit_button = Button(self.button_width, self.button_height, self.x, self.y - 200, 3, 5, 'Q U I T', (1, 1, 1), (235, 60, 50, 255))

    def draw(self):
        self.pop_up.draw()
        self.title.draw()
        self.start_button.draw()
        self.resume_button.draw()
        self.quit_button.draw()

    
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