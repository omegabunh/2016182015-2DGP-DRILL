from pico2d import *
import game_framework


class Brick:
    image = None

    def __init__(self):
        if Brick.image is None:
            self.image = load_image('brick180x40.png')
        self.x, self.y = 1600 // 2, 180
        self.velocity = 200
        self.side = 1

    def update(self):
        if self.x > 1500:
            self.side = -1
        elif self.x < 100:
            self.side = 1
        self.x += self.velocity * game_framework.frame_time * self.side

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20
