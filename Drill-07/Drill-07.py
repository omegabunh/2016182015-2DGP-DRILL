from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0,799), 599
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y > 70:
            self.y -= random.randint(1, 20)
        elif self.x < 70:
            self.y = 70
    def draw(self):
        self.image.draw(self.x, self.y)
class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0,799), 599
        self.image = load_image('ball21x21.png')
    def update(self):
        if self.y > 60:
            self.y -= random.randint(1, 20)
        elif self.x < 60:
            self.y = 60
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

team = [Boy() for i in range(11)]
grass = Grass()
t = random.randint(3, 17)
bigball = [BigBall() for i in range(20 - t)]
smallball = [SmallBall() for i in range(t)]
running = True
# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for Sball in smallball:
        Sball.update()
    for Bball in bigball:
        Bball.update()
    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()
    for Sball in smallball:
        Sball.draw()
    for Bball in bigball:
        Bball.draw()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()