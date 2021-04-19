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
            if self.player_y_pos_in_screen(self.player.y, '+'):
                self.player.y += self.step_size
        if key == 'A':
            if self.player_x_pos_in_screen(self.player.x, '-'):
                self.player.x -= self.step_size
        if key == 'S':
            if self.player_y_pos_in_screen(self.player.y, '-'):
                self.player.y -= self.step_size
        if key == 'D':
            if self.player_x_pos_in_screen(self.player.x, '+'):
                self.player.x += self.step_size
        self.player.draw(self.player.x, self.player.y)


    def player_x_pos_in_screen(self, x, operator):
        new_x = 0
        if operator == '-':
            new_x = x - self.step_size
        elif operator == '+':
            new_x = x + self.step_size
        
        if new_x > 0:
            if new_x + self.player.image_width <= self.screen_width:
                return True
            return False
    
    def player_y_pos_in_screen(self, y, operator):
        new_y = 0
        if operator == '-':
            new_y = y - self.step_size
        elif operator == '+':
            new_y = y + self.step_size
        
        if new_y > 0:
            if new_y + self.player.image_height <= self.screen_height:
                return True
            return False