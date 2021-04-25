import random

from pyglet import image

from objects.enemy import Enemy
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

        self.score = 0
        self.hitbox_handler = HitboxHandler(self.background)
        self.generate_enemies(self.current_level) # spawn enemies
        self.increase_level = increase_level

    def handle_enemies(self, bullets, hud, dt):
        self.hud = hud
        for index, enemy in enumerate(self.enemies):
            self.check_for_collisions(enemy, index, bullets)
            if HITBOX_ENABLED:
                self.hitbox_handler.handle_hitboxes(enemy, index)
            self.adjust_enemy_position(enemy, index, dt)

    def generate_enemies(self, level):
        dummy_enemy = Enemy(0, 100, 1, 1, self.background, self.current_level)
        if TEST:
            for _ in range(1):
                enemy_speed = random.randint(1, 100)
                x = random.randint(10, self.screen_width - int(dummy_enemy.image_width))
                y = self.screen_height
                newEnemy = Enemy(enemy_speed, 100, x, y, self.background, self.current_level)
                if HITBOX_ENABLED:
                    self.hitbox_handler.generate_hitbox_for_enemy(newEnemy)
                self.enemies.append(newEnemy)
        else:
            for _ in range(level['enemy_amount']):
                max_speed = level['enemy_speed']
                enemy_speed = random.randint(10, max_speed) 
                # TODO: Change this later to match idea:
                x = random.randint(1, self.screen_width - int(dummy_enemy.image_width))
                y = self.screen_height
                newEnemy = Enemy(enemy_speed, 100, x, y, self.background, self.current_level)
                if HITBOX_ENABLED:
                    self.hitbox_handler.generate_hitbox_for_enemy(newEnemy)
                self.enemies.append(newEnemy)


    def adjust_enemy_position(self, enemy, index, dt):
        if enemy.y_pos <= 0:
            self.enemies.pop(index)
        else:
            enemy.draw(enemy.x_pos, enemy.y_pos)
            enemy.update(dt)

    def check_for_collisions(self, enemy, index, bullets):
        for b_index, bullet in enumerate(bullets):
            if (bullet.x >= int(enemy.x_pos)) and (bullet.x <= int(enemy.x_pos) + (enemy.image_width)):
                if (bullet.y >= int(enemy.y_pos)) and (bullet.y <= int(enemy.y_pos) + (enemy.image_height)):
                    if enemy.health > 0:
                        enemy.health -= bullet.damage
                        bullets.pop(b_index) # fly further if enemy was killed
                    if enemy.health <= 0:
                        self.enemies.pop(index)
                        self.hud.update(self.current_level)
                        if HITBOX_ENABLED:
                            self.hitbox_handler.delete_hitbox(index)