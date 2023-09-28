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
def draw_hands():
    global hand_coord
    for a in range(0, len(hand_coord) , 2):
        hand_arrow.draw(hand_coord[a], hand_coord[a + 1])


running = True
hand_coord = []
frame = 0
now_boy_x, now_boy_y, past_boy_x, past_boy_y = 1280 // 2, 1024 // 2, 1280 // 2, 1024 // 2

while running:

    handle_events()

    if len(hand_coord) != 0:
        for i in range(0, 50+1):
            clear_canvas()
            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            handle_events()
            t = i / 50
            now_boy_x = (1 - t) * past_boy_x + t * hand_coord[0]
            now_boy_y = (1 - t) * past_boy_y + t * hand_coord[1]
            frame = (frame + 1) % 8
            draw_hands()
            if hand_coord[0] > now_boy_x:
                character.clip_draw(frame * 100, 100, 100, 100, now_boy_x, now_boy_y)
            else:
                character.clip_draw(frame * 100, 0, 100, 100, now_boy_x, now_boy_y)
            update_canvas()
            delay(0.01)
    else:
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, now_boy_x, now_boy_y)
        update_canvas()
    del hand_coord[0:2]
    past_boy_x = now_boy_x
    past_boy_y = now_boy_y

close_canvas()
