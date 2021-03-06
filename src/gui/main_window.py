import pyglet
from pyglet.gl import *
from gui.menu.end_screen import EndScreen

from handler.event_handler import GameEventHandler
from handler.enemy_handler import EnemyHandler
from handler.player_handler import PlayerHandler
from handler.bullet_handler import BulletHandler
from objects.player import Player
from gui.hud.hud import HUD
from gui.menu.menu import Menu

class MainWindow(pyglet.window.Window):
    # TODO: add settings file where width, height etc can be stored?
    def __init__(self, cursor, levels, pause_menu, background, *args, **kwrgs):
        super().__init__(*args, **kwrgs, vsync=False)
        pyglet.gl.glClearColor(0.7, 0.6, 0.4, 0.29)
        self.cursor = cursor
        self.levels = levels
        self.current_level = 0
        self.level_background = background
        self.level_active = False
        self.enemy_handler = self.spawn_enemies_for_level(self.current_level)
        

        self.player = Player(self.width / 2, 40, self.level_background)
        self.bullet_handler = BulletHandler(self.player, self.level_background)
        self.player_handler = PlayerHandler(self.player, self.width, self.height, self.bullet_handler, self.cursor)

        self.hud = HUD(self.width, self.height, len(self.enemy_handler.enemies), (255, 69, 0, 255))
        self.pause_menu = pause_menu
        self.menu_visible = True
        self.end_screen = EndScreen(self.width, self.height, 0, 0, 0)
        self.end_screen_visible = False

        self.mouse_x = 0
        self.mouse_y = 0

        self.game_event_handler = GameEventHandler(
                                    self.update_mouse_coordinates, 
                                    self.toggle_menu, 
                                    self.mouse_click_tracker, 
                                    self.mouse_motion_tracker,
                                    self.player_handler.player_action_handler,
                                    )
        self.push_handlers(self.game_event_handler)

    
    def update_mouse_coordinates(self, x, y):
        self.mouse_x = x
        self.mouse_y = y


    def toggle_menu(self):
        self.menu_visible = not self.menu_visible

    
    def on_resize(self, width, height):
        self.width = width
        self.height = height

        # reinitialize score with current values:
        current_score = self.hud.score.value
        current_kill_count = self.hud.kill_count.killed
        self.hud = HUD(self.width, self.height, self.levels[self.current_level]['enemy_amount'], (255, 69, 0, 255))
        self.hud.score.update_score(current_score)
        self.hud.kill_count.killed = current_kill_count

        # reinit player and player_handler
        self.player = Player(self.width / 2, 40, self.level_background)
        self.bullet_handler = BulletHandler(self.player, self.level_background)
        self.player_handler = PlayerHandler(self.player, self.width, self.height, self.bullet_handler, self.cursor)

        # reinit menus:
        self.pause_menu = Menu(self.width, self.height)
        # add handlers:
        self.pop_handlers()
        self.game_event_handler = GameEventHandler(
                                    self.update_mouse_coordinates, 
                                    self.toggle_menu, 
                                    self.mouse_click_tracker, 
                                    self.mouse_motion_tracker,
                                    self.player_handler.player_action_handler,
                                    )
        self.push_handlers(self.game_event_handler)
        return super().on_resize(width, height)

    
    def mouse_click_tracker(self, x, y):
        if self.menu_visible:
            if self.pause_menu.button_was_clicked(x, y, self.pause_menu.start_button):
                print('START CLICKED')
                self.enemy_handler = self.spawn_enemies_for_level()
                self.current_level = 0
                self.hud.kill_count.reset_counter(len(self.enemy_handler.enemies))
                self.hud.score.reset_score()
                self.toggle_menu()
            if self.pause_menu.button_was_clicked(x, y, self.pause_menu.resume_button) and self.level_active:
                print('RESUME CLICKED')
                self.toggle_menu()
            if self.pause_menu.button_was_clicked(x, y, self.pause_menu.quit_button):
                print('QUIT CLICKED')
                self.game_event_handler.alive = 0
        if self.end_screen_visible:
            if self.end_screen.button_was_clicked(x, y, self.end_screen.menu_button):
                print('MENU CLICKED')
                self.end_screen_visible = False
                self.toggle_menu()


    def weapon_tracker(self):
        self.bullet_handler()
        pass
    
    def mouse_motion_tracker(self, x, y):
        if self.menu_visible:
            if self.pause_menu.button_was_touched(x, y, self.pause_menu.start_button):
                self.pause_menu.start_button.hovered()
            else:
                self.pause_menu.start_button.not_hovered()
            if self.pause_menu.button_was_touched(x, y, self.pause_menu.resume_button) and self.level_active:
                self.pause_menu.resume_button.hovered()
            else:
                self.pause_menu.resume_button.not_hovered()
            if self.pause_menu.button_was_touched(x, y, self.pause_menu.quit_button):
                self.pause_menu.quit_button.hovered()
            else:
                self.pause_menu.quit_button.not_hovered()
        if self.end_screen_visible:
            if self.end_screen.button_was_touched(x, y, self.end_screen.menu_button):
                self.end_screen.menu_button.hovered()
            else:
                self.end_screen.menu_button.not_hovered()


    def spawn_enemies_for_level(self, level_num=0):
        # TODO: Load levels from JSON File.
        self.level_active = True
        return EnemyHandler(self.width, self.height, self.level_background, self.levels[level_num], self.increase_level) # Put current level in it.

    
    def increase_level(self, current_level):
        print(f'Increasing to Level {current_level + 1}')
        try:
            self.next_level = current_level + 1
            self.current_level = self.next_level
            self.enemy_handler = self.spawn_enemies_for_level(self.next_level)
            self.hud.kill_count.update_enemy_amount(self.levels[self.next_level]['enemy_amount'])
            self.hud.level_info.update_level()
        except Exception:
            # TODO: Add End_Game Message.
            # traceback.print_exc()
            print('\nALL LEVELS COMPLETED!')
            self.hud.level_info.reset_level()
            self.end_screen = EndScreen(self.width, self.height, self.hud.score.value, self.hud.kill_count.killed, self.hud.kill_count.enemy_amount)
            self.level_active = False
            self.end_screen_visible = True


    def render(self, dt):
        self.clear()

        if not self.menu_visible and self.level_active:
            self.check_if_level_ended()
            self.set_mouse_visible(False)
            self.enemy_handler.handle_enemies(self.bullet_handler.bullets, self.hud, dt)

            self.cursor.draw(self.mouse_x, self.mouse_y)
            self.player_handler.handle_player_action(self.game_event_handler.keys)
            self.bullet_handler.handle_bullets(self.width, self.height)
            self.level_background.draw()
            self.hud.draw()
        elif self.end_screen_visible:
            self.set_mouse_visible(True)
            self.end_screen.draw()
        else:
            self.pause_menu.draw()
            self.set_mouse_visible(True)

        self.flip()


    def update(self, dt):
        while self.game_event_handler.alive == 1:
            self.render(dt)
            self.dispatch_events()
        self.close()

    
    def check_if_level_ended(self):
        if len(self.enemy_handler.enemies) < 1:
            self.level_active = False
            self.increase_level(self.current_level)