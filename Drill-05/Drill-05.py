from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global _x, _y
    global side
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDL_MOUSEMOTION:
            _x, _y = event.x + 20, KPU_HEIGHT - 1 - event.y - 30
        elif event.button == SDL_BUTTON_LEFT:
            if x < event.x:
                x, y = event.x, KPU_HEIGHT - 1 - event.y
                side = 1
            elif x > event.x:
                x, y = event.x, KPU_HEIGHT - 1 - event.y
                side = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
show_cursor()
side = 0
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * side, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()




