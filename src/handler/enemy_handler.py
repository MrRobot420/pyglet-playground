import random
from objects.enemy import Enemy

class EnemyHandler():
    def __init__(self, screen_width, screen_height, background):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = background
        self.enemies = []
        self.mouse_x = 0
        self.mouse_y = 0
        self.score = 0
        self.generate_enemies() # spawn enemies


    def handle_enemies(self, mouse_x, mouse_y, score, dt):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.score = score
        for index, enemy in enumerate(self.enemies):
            self.adjust_enemy_position(enemy, index, dt)
            self.check_for_collisions(enemy, index)


    def generate_enemies(self, amount=10):
        for index in range(amount):
            self.enemies.append(Enemy(random.randint(1, 10),
                                      100,
                                      random.randint(5, 30),
                                      random.randint(1, self.screen_width),
                                      self.screen_height,
                                      self.background))


    def adjust_enemy_position(self, enemy, index, dt):
        if enemy.y_pos <= 0:
            self.enemies.pop(index)
            self.enemies.append(
                Enemy(random.randint(1, 10),
                        100,
                        random.randint(5, 30),
                        random.randint(1, self.screen_width),
                        self.screen_height,
                        self.background)
            )
        else:
            enemy.draw(enemy.x_pos, enemy.y_pos)
            enemy.update(dt)


    def check_for_collisions(self, enemy, index):
        if (int(enemy.x_pos) >= self.mouse_x) & (int(enemy.x_pos) <= self.mouse_x + (enemy.image_width * enemy.scale)):
            if (int(enemy.y_pos) >= int(self.mouse_y)) & (int(enemy.y_pos) <= self.mouse_y + (enemy.image_height * enemy.scale)):
                self.enemies.pop(index)
                self.score.updateScore()