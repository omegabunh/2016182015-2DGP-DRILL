import game_framework
from pico2d import *

import game_world

# Boy Run Speed
# fill expressions correctly

#30cm당 10픽셀
#새 몸통의 크기 약 2.3m
#새 시속 20KM
#1초에 날개짓 4번

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}


# Boy States

class IdleState:

    @staticmethod
    def enter(bird, event):
        if event == RIGHT_DOWN:
            bird.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            bird.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            bird.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            bird.velocity += RUN_SPEED_PPS
        bird.timer = 1000

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        bird.timer -= 1


    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw((int(bird.frame) % 5) * 182, (2 - (int(bird.frame) // 5)) * 168, 182, 168,
                                 bird.x, bird.y)
        else:
            bird.image.clip_composite_draw((int(bird.frame) % 5) * 182, (2 - (int(bird.frame) // 5)) * 168, 182,
                                           168, 0.0, 'h', bird.x, bird.y, 182, 168)


class RunState:

    @staticmethod
    def enter(bird, event):
        if event == RIGHT_DOWN:
            bird.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            bird.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            bird.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            bird.velocity += RUN_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)



    @staticmethod
    def exit(bird, event):
      pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw((int(bird.frame) % 5) * 182, (2 - (int(bird.frame) // 5)) * 168, 182, 168,
                                 bird.x, bird.y)
        else:
            bird.image.clip_composite_draw((int(bird.frame) % 5) * 182, (2 - (int(bird.frame) // 5)) * 168, 182,
                                           168, 0.0, 'h', bird.x, bird.y, 182, 168)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState},

}

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

