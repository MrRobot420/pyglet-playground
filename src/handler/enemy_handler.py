import random
from objects.enemy import Enemy
from objects.hitbox import Hitbox

HITBOX_ENABLED = False
class EnemyHandler():
    def __init__(self, screen_width, screen_height, background):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = background
        self.enemies = []
        self.hitboxes = []
        self.inner_hitboxes = []
        self.mouse_x = 0
        self.mouse_y = 0
        self.score = 0
        self.generate_enemies() # spawn enemies


    def handle_enemies(self, mouse_x, mouse_y, score, dt):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.score = score
        for index, enemy in enumerate(self.enemies):
            if HITBOX_ENABLED:
                self.handle_hitboxes(enemy, index)
            self.adjust_enemy_position(enemy, index, dt)
            self.check_for_collisions(enemy, index)

    
    def handle_hitboxes(self, enemy, index):
        hitbox = self.hitboxes[index]
        inner_hitbox = self.inner_hitboxes[index]
        hitbox.adjust_hitbox_position(enemy, hitbox, index, -2)
        inner_hitbox.adjust_hitbox_position(enemy, inner_hitbox, index, 0)


    def generate_enemies(self, amount=100):
        for index in range(amount):
            enemySpeed = random.randint(1, 100)
            x = random.randint(1, self.screen_width)
            y = self.screen_height
            newEnemy = Enemy(enemySpeed, 100, x, y, self.background)
            if HITBOX_ENABLED:
                self.generate_hitbox_for_enemy(newEnemy)
            self.enemies.append(newEnemy)

    
    def generate_hitbox_for_enemy(self, newEnemy):
        self.hitboxes.append(Hitbox(newEnemy.speed, newEnemy.image_width + 4, newEnemy.image_height + 4, newEnemy.x_pos - 5, newEnemy.y_pos - 5, self.background, (255, 100, 120)))
        self.inner_hitboxes.append(Hitbox(newEnemy.speed, newEnemy.image_width, newEnemy.image_height, newEnemy.x_pos, newEnemy.y_pos, self.background, (230, 230, 230)))



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
                self.score.updateScore()