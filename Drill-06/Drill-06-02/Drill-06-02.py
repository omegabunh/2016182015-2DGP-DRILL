from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH,KPU_HEIGHT)

def move(p1, p2, p3):
    global x, y, side
    global frame
    if p1[0] < p2[0]:
        side = 1
    elif p1[0] > p2[0]:
        side = 0

    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * side, 100, 100, x, y)
        for i in range(0, 10):
            character.clip_draw(frame * 100, 100 * side, 100, 100, p3[0], p3[1])
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
x, y = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)
side = 1
frame = 0
size = 10
points = [(random.randint(0 + 100, KPU_WIDTH-100), random.randint(0+100, KPU_HEIGHT-100)) for i in range(size)]
n = 1

while True:
    #p1, p2, p3, p4 = points[n-3], points[n-2], points[n-1], points[n]
    p1, p2, p3 = points[n - 2], points[n - 1], points[n]
    n = (n + 1) % size
    move(p1, p2, p3)
    #move(p1, p2, p3, p4)

close_canvas()