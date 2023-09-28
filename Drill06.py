from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running, hand_coord
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                hand_coord.append(event.x)
                hand_coord.append(TUK_HEIGHT - 1 - event.y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
hand_coord = []
now_boy_x, now_boy_y, past_boy_x, past_boy_y = 1280 // 2, 1024 // 2, 1280 // 2, 1024 // 2

while running:

