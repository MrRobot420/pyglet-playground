# Documentation for the pyglet playground

### How to play this game
 - create venv using virtualenv
 - activate env and run ````pip install -r requirements.txt````
 - then from your projects root ```` cd src && python game.py````

## 10.04.2021:

### Basic Window

```python
import pyglet

class MainWindow(pyglet.window.Window):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)

if __name__ == '__main__':
    window = MainWindow(640, 480, 'Game Name', resizable=True)
    pyglet.app.run()
```

---

### Mouse Events
See: https://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html

```python
import pyglet
from pyglet.window import mouse

class MouseMovementHandler():
    '''
    :possible buttons:
        `mouse.LEFT`
        `mouse.MIDDLE`
        `mouse.RIGHT`
    :modifiers:
        for `keyboard events`
    '''
    def __init__(self):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        '''
        Triggered when mouse moves.\n
        x and y point to current position. NOTE: starting point is lower left corner of the window.\n
        dx and dy measure the distance the mouse had to travel on each axis to get to the current point.
        '''
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_mouse_enter(x, y):
        '''Triggered when mouse enters the window.'''
        pass

    def on_mouse_leave(x, y):
        '''Triggered when mouse leaves the window.'''
        pass

    def on_mouse_scroll(x, y, scroll_x, scroll_y):
        pass
```

---

### Cursor Types

```python
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

# CHANGE THE CURSOR TO SYSTEM CURSORS
if __name__ == '__main__':
    window = MainWindow(640, 480, 'Game Name', resizable=True)
    # window.set_mouse_visible(False) # Hide the mouse cursor
    cursor = window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
    window.set_mouse_cursor(cursor)
    pyglet.app.run()

# USE YOUR OWN IMAGE MOUSE CURSOR
if __name__ == '__main__':
    window = MainWindow(640, 480, 'Game Name', resizable=True)
    image = pyglet.image.load('./resources/cursor/red_cross.png')
    cursor = pyglet.window.ImageMouseCursor(image, 16, 16)
    window.set_mouse_cursor(cursor)
    pyglet.app.run()

```