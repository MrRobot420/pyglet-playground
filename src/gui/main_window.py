import pyglet
from pyglet.gl import *

from handler.event_handler import GameEventHandler
from handler.enemy_handler import EnemyHandler

class MainWindow(pyglet.window.Window):
    def __init__(self, cursor, enemy_handler, hud, pause_menu, background, *args, **kwrgs):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)
        self.cursor = cursor
        self.enemy_handler = enemy_handler
        self.hud = hud
        self.pause_menu = pause_menu
        self.menu_visible = True
        self.level_background = background

        self.mouse_x = 0
        self.mouse_y = 0

        self.game_event_handler = GameEventHandler(self.update_mouse_coordinates, self.toggle_menu, self.mouse_click_tracker)
        self.push_handlers(self.game_event_handler)

    
    def update_mouse_coordinates(self, x, y):
        self.mouse_x = x
        self.mouse_y = y


    def toggle_menu(self):
        self.menu_visible = not self.menu_visible

    
    def mouse_click_tracker(self, x, y):
        if self.menu_visible:
            if self.pause_menu.button_was_clicked(x, y, self.pause_menu.start_button):
                # TODO: start (new) game.
                self.enemy_handler = EnemyHandler(self.width, self.height, self.level_background)
                self.hud.kill_count.reset_counter(len(self.enemy_handler.enemies))
                self.hud.score.reset_score()
                self.toggle_menu()
            if self.pause_menu.button_was_clicked(x, y, self.pause_menu.resume_button):
                self.toggle_menu()


    def on_draw(self):
        dt = pyglet.clock.tick()
        self.render(dt)


    def render(self, dt):
        self.clear()

        if not self.menu_visible:
            self.set_mouse_visible(False)
            self.enemy_handler.handle_enemies(self.mouse_x, self.mouse_y, self.hud, dt)

            self.hud.draw()
            self.cursor.draw(self.mouse_x, self.mouse_y)
            self.level_background.draw()
        else:
            self.pause_menu.draw()
            self.set_mouse_visible(True)

        self.flip()


    def update(self, dt):
        while self.game_event_handler.alive == 1:
            self.render(dt)
            self.dispatch_events()
        self.close()