import random

from objects.enemy import Enemy
from objects.hitbox import Hitbox
from handler.hitbox_handler import HitboxHandler

HITBOX_ENABLED = False
TEST = False
class EnemyHandler():
    def __init__(self, screen_width, screen_height, background, level, increase_level):
        print('spawning enemies.')
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = background
        self.enemies = []
        self.current_level = level

        self.mouse_x = 0
        self.mouse_y = 0
        self.score = 0
        self.hitbox_handler = HitboxHandler(self.background)
        self.generate_enemies(self.current_level) # spawn enemies
        self.increase_level = increase_level

    def handle_enemies(self, mouse_x, mouse_y, hud, dt):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.hud = hud
        for index, enemy in enumerate(self.enemies):
            if HITBOX_ENABLED:
                self.hitbox_handler.handle_hitboxes(enemy, index)
            self.adjust_enemy_position(enemy, index, dt)
            self.check_for_collisions(enemy, index)

    def generate_enemies(self, level):
        dummy_enemy = Enemy(0, 100, 1, 1, self.background, 'axolotl')
        if TEST:
            for _ in range(1):
                enemy_speed = random.randint(1, 100)
                x = random.randint(10, self.screen_width - int(dummy_enemy.image_width))
                y = self.screen_height
                newEnemy = Enemy(enemy_speed, 100, x, y, self.background, 'axolotl')
                if HITBOX_ENABLED:
                    self.hitbox_handler.generate_hitbox_for_enemy(newEnemy)
                self.enemies.append(newEnemy)
        else:
            for _ in range(level['enemy_amount']):
                max_speed = level['enemy_speed']
                enemy_speed = random.randint(10, max_speed) 
                enemy_type = level['enemy_type']
                # TODO: Change this later to match idea:
                x = random.randint(1, self.screen_width - int(dummy_enemy.image_width))
                y = self.screen_height
                newEnemy = Enemy(enemy_speed, 100, x, y, self.background, enemy_type)
                if HITBOX_ENABLED:
                    self.hitbox_handler.generate_hitbox_for_enemy(newEnemy)
                self.enemies.append(newEnemy)


    def adjust_enemy_position(self, enemy, index, dt):
        if enemy.y_pos <= 0:
            self.enemies.pop(index)
        else:
            enemy.draw(enemy.x_pos, enemy.y_pos)
            enemy.update(dt)

    def check_for_collisions(self, enemy, index):
        if (self.mouse_x >= int(enemy.x_pos)) and (self.mouse_x <= int(enemy.x_pos) + (enemy.image_width)):
            if (self.mouse_y >= int(enemy.y_pos)) and (self.mouse_y <= int(enemy.y_pos) + (enemy.image_height)):
                self.enemies.pop(index)
                self.hud.update(self.current_level)