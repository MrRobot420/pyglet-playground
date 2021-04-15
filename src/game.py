import pyglet

from gui.main_window import MainWindow
from gui.elements.cursor import Cursor
from gui.hud.hud import HUD
from handler.enemy_handler import EnemyHandler

class Game:
    def __init__(self):
        background = pyglet.graphics.Batch()
        width = 1280
        height = 960
        
        cursor = Cursor(background)
        enemy_handler = EnemyHandler(width, height, background) # Put current level in it.
        hud = HUD(width, height, len(enemy_handler.enemies))

        game_window = MainWindow(cursor, enemy_handler, hud, width, height, 'Shoot Em’ Up!', resizable=True)
        game_window.set_mouse_visible(False)  # Hide the mouse cursor

        pyglet.clock.schedule_interval(game_window.update, 1/60.0)
        pyglet.app.run()

if __name__ == '__main__':
    Game()