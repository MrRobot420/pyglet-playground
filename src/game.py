import pyglet

from gui.main_window import MainWindow
from gui.elements.cursor import Cursor
from gui.hud.hud import HUD
from gui.menu.menu import Menu
from handler.enemy_handler import EnemyHandler

class Game:
    def __init__(self):
        self.background = pyglet.graphics.Batch()
        self.width = 1280
        self.height = 960
        
        self.cursor = Cursor(self.background)
        self.enemy_handler = EnemyHandler(self.width, self.height, self.background) # Put current level in it.
        self.hud = HUD(self.width, self.height, len(self.enemy_handler.enemies))
        self.pause_menu = Menu(self.width, self.height)
        # TODO: add settings file where width, height etc can be stored?

        self.game_window = MainWindow(self.cursor, self.enemy_handler, self.hud, self.pause_menu, self.background, self.width, self.height, 'Shoot Em’ Up!', resizable=True)
        self.game_window.set_mouse_visible(False)  # Hide the mouse cursor

        pyglet.clock.schedule_interval(self.game_window.update, 1/60.0)
        pyglet.app.run()

if __name__ == '__main__':
    Game()