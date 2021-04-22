from datetime import datetime as dtime
from objects.bullet import Bullet

class BulletHandler():
    def __init__(self, player, background):
        self.background = background
        self.player = player
        self.bullets = []
        self.last_shot = 0
        self.timeout = 0.25
    
    def add_bullet(self, cursor):
        current_shot = dtime.now().timestamp()
        if (current_shot - self.last_shot) > self.timeout:
            print('Shooting.')
            start_x = self.player.x
            start_y = self.player.y + self.player.image_height
            target_x = cursor.x
            target_y = cursor.y
            print(f'Aiming at target: {target_x}, {target_y}')
            new_bullet = Bullet(start_x, start_y, target_x, target_y, self.background)
            self.bullets.append(new_bullet)
            self.last_shot = current_shot

    
    def handle_bullets(self, dt, width, height):
        current_time = dtime.now().timestamp()
        for index, bullet in enumerate(self.bullets):
            time_factor = current_time - bullet.start_time
            if self.bullet_in_display(bullet, width, height):
                target_x = bullet.target_x
                target_y = bullet.target_y
                # TODO: Add velocity to bullet. Add turn to bullet. All based on cursor position!
                start_x = bullet.start_x
                start_y = bullet.start_y
                x_diff = target_x - start_x
                y_diff = target_y - start_y
                bullet.update_bullet(x_diff * time_factor, y_diff * time_factor)
            else:
                self.bullets.pop(index)


    def bullet_in_display(self, bullet, width, height):
        if bullet.x > 0 and bullet.x + bullet.image_width <= width:
            if bullet.y > 0 and bullet.y + bullet.image_height <= height:
                return True
            return False