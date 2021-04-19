
class PlayerHandler:
    def __init__(self, player):
        self.player = player
        self.step_size = 10


    def player_action_handler(self, key):
        if key == 'W':
            self.player.y += self.step_size
        if key == 'A':
            self.player.x -= self.step_size
        if key == 'S':
            self.player.y -= self.step_size
        if key == 'D':
            self.player.x += self.step_size
        self.player.draw(self.player.x, self.player.y)
