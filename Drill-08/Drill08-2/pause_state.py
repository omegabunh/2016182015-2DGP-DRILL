import main_state
import game_framework
from pico2d import*

pause = None
image = None
cnt = 0


def enter():
    global image
    image = load_image('pause.png')

def exit():
    global pause
    del(pause)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()
def update():
    global cnt
    if cnt == 0:
        cnt = 1
    else:
        cnt = 0

def draw():
    global cnt
    clear_canvas()
    if (cnt == 0):
        image.draw(400, 300)
    main_state.grass.draw()
    main_state.boy.draw()
    delay(0.3)
    update_canvas()

