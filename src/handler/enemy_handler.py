import random
from objects.enemy import Enemy
from objects.hitbox import Hitbox

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
            hitbox = self.hitboxes[index]
            inner_hitbox = self.inner_hitboxes[index]
            self.adjust_hitbox_position(enemy, hitbox, index, -5)
            self.adjust_hitbox_position(enemy, inner_hitbox, index, 0)
            self.adjust_enemy_position(enemy, index, dt)
            self.check_for_collisions(enemy, index)


    def generate_enemies(self, amount=100):
        for index in range(amount):
            enemySpeed = random.randint(1, 100)
            x = random.randint(1, self.screen_width)
            y = self.screen_height
            newEnemy = Enemy(enemySpeed, 100, x, y, self.background)
            self.hitboxes.append(Hitbox(enemySpeed, newEnemy.image_width + 10, newEnemy.image_height + 10, x - 5, y - 5, self.background, (255, 55, 55)))
            self.inner_hitboxes.append(Hitbox(enemySpeed, newEnemy.image_width, newEnemy.image_height, x, y, self.background, (240, 240, 240)))
            self.enemies.append(newEnemy)


    def adjust_enemy_position(self, enemy, index, dt):
        if enemy.y_pos <= 0:
            self.enemies.pop(index)
        else:
            enemy.draw(enemy.x_pos, enemy.y_pos)
            enemy.update(dt)

    
    def adjust_hitbox_position(self, enemy, hitbox, index, diff):
        if hitbox.y_pos <= 0:
            self.hitboxes.pop(index)
        else:
            hitbox.draw(enemy.x_pos + diff, enemy.y_pos + diff)
            


    def check_for_collisions(self, enemy, index):
        if (self.mouse_x >= int(enemy.x_pos)) and (self.mouse_x <= int(enemy.x_pos) + (enemy.image_width)):
            if (self.mouse_y >= int(enemy.y_pos)) and (self.mouse_y <= int(enemy.y_pos) + (enemy.image_height)):
                self.enemies.pop(index)
                self.score.updateScore()