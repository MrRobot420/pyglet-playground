from pyglet.window import key

class PlayerHandler:
    def __init__(self, player, width, height):
        self.screen_width = width
        self.screen_height = height
        self.player = player
        self.step_size = 5

    def handle_player_action(self, keys):
        if key.W in keys:
            self.player_action_handler('W')
        if key.A in keys:
            self.player_action_handler('A')
        if key.S in keys:
            self.player_action_handler('S')
        if key.D in keys:
            self.player_action_handler('D')


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
