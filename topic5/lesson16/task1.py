class Vec2I:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Turtle:

    def __init__(self, pos, init_s):
        self.pos = pos
        self.s = init_s

    def go_up(self):
        self.pos.y += self.s

    def go_down(self):
        self.pos.y -= self.s

    def go_left(self):
        self.pos.x -= self.s

    def go_right(self):
        self.pos.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s == 1:
            raise ValueError("s must be greater than 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.pos.x)
        dy = abs(y2 - self.pos.y)
        return (dx // self.s) + (dy // self.s)
