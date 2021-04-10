import pyglet

'''
Available system mouse cursors:
CURSOR_DEFAULT
CURSOR_CROSSHAIR
CURSOR_HAND	
CURSOR_HELP
CURSOR_NO
CURSOR_SIZE
CURSOR_SIZE_DOWN
CURSOR_SIZE_DOWN_LEFT
CURSOR_SIZE_DOWN_RIGHT
CURSOR_SIZE_LEFT
CURSOR_SIZE_LEFT_RIGHT
CURSOR_SIZE_RIGHT
CURSOR_SIZE_UP
CURSOR_SIZE_UP_DOWN
CURSOR_SIZE_UP_LEFT
CURSOR_SIZE_UP_RIGHT
CURSOR_TEXT
CURSOR_WAIT
CURSOR_WAIT_ARROW
'''

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)

if __name__ == '__main__':
    window = MainWindow(640, 480, 'Game Name', resizable=True)
    # window.set_mouse_visible(False) # Hide the mouse cursor
    cursor = window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
    window.set_mouse_cursor(cursor)
    pyglet.app.run()