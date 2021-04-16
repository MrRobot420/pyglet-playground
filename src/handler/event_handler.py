import pyglet

key = pyglet.window.key
from pyglet.window import mouse

class GameEventHandler:
    def __init__(self, upd_coords, menu_toggler, click_tracker):
        self.keys = {}
        self.alive = 1
        self.update_mouse_coordinates = upd_coords
        self.toggle_menu = menu_toggler
        self.mouse_click_tracker = click_tracker
    

    def on_close(self):
        self.alive = 0


    def on_mouse_motion(self, x, y, dx, dy):
        self.update_mouse_coordinates(x, y)


    def on_key_release(self, symbol, modifiers):
        try:
            del self.keys[symbol]
        except:
            pass


    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.mouse_click_tracker(x, y)


    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:  # [ESC]
            self.alive = 0
        if symbol == key.TAB:
            self.toggle_menu()

        self.keys[symbol] = True