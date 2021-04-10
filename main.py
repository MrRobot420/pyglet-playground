import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)


if __name__ == '__main__':
    window = MainWindow(640, 480, 'Game Name', resizable=True)
    pyglet.app.run()