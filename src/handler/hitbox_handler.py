from objects.hitbox import Hitbox

class HitboxHandler:
    def __init__(self, background):
        self.background = background
        self.hitboxes = []
        self.inner_hitboxes = []

    def generate_hitbox_for_enemy(self, newEnemy):
        self.hitboxes.append(Hitbox(newEnemy.speed, newEnemy.image_width + 4, newEnemy.image_height + 4, newEnemy.x_pos - 5, newEnemy.y_pos - 5, self.background, (255, 100, 120)))
        self.inner_hitboxes.append(Hitbox(newEnemy.speed, newEnemy.image_width, newEnemy.image_height, newEnemy.x_pos, newEnemy.y_pos, self.background, (230, 230, 230)))

    def handle_hitboxes(self, enemy, index):
        try: 
            hitbox = self.hitboxes[index]
            inner_hitbox = self.inner_hitboxes[index]
            hitbox.adjust_hitbox_position(enemy, hitbox, index, -2)
            inner_hitbox.adjust_hitbox_position(enemy, inner_hitbox, index, 0)
        except Exception:
            pass

    def delete_hitbox(self, index):
        self.hitboxes.pop(index)
        self.inner_hitboxes.pop(index)