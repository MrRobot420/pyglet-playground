import pyglet
import json

from gui.main_window import MainWindow
from gui.elements.cursor import Cursor
from gui.menu.menu import Menu
from handler.resource_handler import ResourceHandler
from objects.player import Player

class Game:
    def __init__(self):
        self.background = pyglet.graphics.Batch()
        self.width = 1280
        self.height = 960

        with open('./level/levels.json', "r") as levels:
            self.levels = json.load(levels)
        print(self.levels)
        self.resource_handler = ResourceHandler()
        self.resource_handler.load_font()
        
        self.cursor = Cursor(self.background)
        self.pause_menu = Menu(self.width, self.height)
        self.game_window = MainWindow(self.cursor,
                                      self.levels['levels'],
                                      self.pause_menu, 
                                      self.background, 
                                      self.width, 
                                      self.height,
                                      'Shoot Em’ Up!', 
                                      resizable=True)

        self.game_window.set_mouse_visible(False)  # Hide the mouse cursor

        pyglet.clock.schedule_interval(self.game_window.update, 1/240.0)
        pyglet.app.run()

if __name__ == '__main__':
    Game()