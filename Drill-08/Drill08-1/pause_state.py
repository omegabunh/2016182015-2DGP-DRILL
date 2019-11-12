import main_state
import game_framework
from pico2d import*

pause = None
image = None

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
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

