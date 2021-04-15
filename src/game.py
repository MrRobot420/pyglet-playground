import pyglet
from gui.main_window import MainWindow

class Game:
    def __init__(self):
        game_window = MainWindow(1280, 960, 'Game Name', resizable=True)
        game_window.set_mouse_visible(False)  # Hide the mouse cursor
        pyglet.clock.schedule_interval(game_window.update, 1/60.0)
        pyglet.app.run()

if __name__ == '__main__':
    Game()