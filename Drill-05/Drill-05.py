from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global mouseX, mouseY
    global side

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x + 20, KPU_HEIGHT - 1 - event.y - 30
        elif event.button == SDL_BUTTON_LEFT:
            if x < event.x:
                x, y = event.x, KPU_HEIGHT - 1 - event.y
                side = 1
            elif event.x < x:
                x, y = event.x, KPU_HEIGHT - 1 - event.y
                side = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_point = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x1, y1 = KPU_WIDTH // 2, KPU_HEIGHT // 2
mouseX, mouseY = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
side = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse_point.draw_now(mouseX, mouseY)
    character.clip_draw(frame * 100, 100 * side, 100, 100, x1, y1)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if x1 < x and y1 < y:
        x1 += (x - x1) / 10
        y1 += (y - y1) / 10
    elif x1 < x and y < y1:
        x1 += (x - x1) / 10
        y1 -= (y1 - y) / 10
    elif x < x1 and y1 < y:
        x1 -= (x1 - x) / 10
        y1 += (y - y1) / 10
    elif x < x1 and y < y1:
        x1 -= (x1 - x) / 10
        y1 -= (y1 - y) / 10

    delay(0.05)

close_canvas()