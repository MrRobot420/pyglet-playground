import pyglet
from main_window import MainWindow

if __name__ == '__main__':
    game_window = MainWindow(1280, 960, 'Game Name', resizable=True)
    pyglet.clock.schedule_interval(game_window.update, 1/60.0)
    game_window.set_mouse_visible(False)  # Hide the mouse cursor
    pyglet.app.run()