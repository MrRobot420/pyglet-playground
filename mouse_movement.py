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