import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, boy):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(1, 1280 - 1), random.randint(1, 1024 - 1)
        self.boy = boy

    def get_bb(self):
        return self.x - 10-self.boy.bg.window_left, self.y - 10 - self.boy.bg.window_bottom, self.x + 10-self.boy.bg.window_left, self.y + 10 -self.boy.bg.window_bottom

    def draw(self):
        self.image.draw(self.x-self.boy.bg.window_left, self.y-self.boy.bg.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

