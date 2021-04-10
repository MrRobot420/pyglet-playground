from pyglet import shapes, clock


class Enemy:
    def __init__(self, speed, health, size, x_pos, y_pos, background):
        self.speed = speed
        self.health = health
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.background = background
        self.clock = clock

    def draw(self, x, y):
        square = shapes.Rectangle(x, y, self.size, self.size, color=(55, 55, 2), batch=self.background)
        square.draw()
        pass

    def update(self):
        print(f"Enemy last update: {self.clock.tick()}")
        self.y_pos -= self.speed * 10 * self.clock.tick()
