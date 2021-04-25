import math

from datetime import datetime as dtime
from objects.bullet import Bullet

class BulletHandler():
    def __init__(self, player, background):
        self.background = background
        self.player = player
        self.bullets = []
        self.last_shot = 0
        self.timeout = 0.25
        self.speed = 10
        self.speed_factor = 100
    

    def add_bullet(self, cursor):
        current_shot = dtime.now().timestamp()
        if (current_shot - self.last_shot) > self.timeout:
            start_x = self.player.x
            start_y = self.player.y + self.player.image_height
            new_bullet = Bullet(start_x, start_y, cursor.x - cursor.width, cursor.y - cursor.height, self.background)
            self.bullets.append(new_bullet)
            self.last_shot = current_shot
            print(f'Shooting at target: {cursor.x}, {cursor.y}')

    
    def handle_bullets(self, width, height):
        current_time = dtime.now().timestamp()
        for index, bullet in enumerate(self.bullets):
            time_factor = current_time - bullet.start_time
            if self.bullet_in_display(bullet, width, height):
                next_x, next_y = self.calculate_next_position(bullet, time_factor)
                bullet.update_bullet(next_x, next_y)
            else:
                self.bullets.pop(index)

    
    def calculate_next_position(self, bullet, time_factor):
        x_diff = int(bullet.target_x) - int(bullet.start_x)
        y_diff = int(bullet.target_y) - int(bullet.start_y)
        
        magnitude = math.sqrt((x_diff**2 + y_diff**2))

        normalized_x = x_diff / magnitude
        normalized_y = y_diff / magnitude

        next_x = bullet.start_x + (normalized_x * time_factor * self.speed_factor * self.speed)
        next_y = bullet.start_y + (normalized_y * time_factor * self.speed_factor * self.speed)

        return next_x, next_y


    def bullet_in_display(self, bullet, width, height):
        if bullet.x > 0 and bullet.x + bullet.image_width <= width:
            if bullet.y > 0 and bullet.y + bullet.image_height <= height:
                return True
            return False