from pico2d import *

WIDTH, HEIGHT = 1280, 1024

IDLE = -1
LEFT, RIGHT = 0, 1
UP, DOWN = 2, 3


def handle_events():
    global quit
    global running
    global dir
    global x, y
    global look
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit = False
        elif event.type == SDL_KEYDOWN:
            running = True
            if event.key == SDLK_ESCAPE:
                quit = False
            elif event.key == SDLK_LEFT:
                look = LEFT
                dir = LEFT
            elif event.key == SDLK_RIGHT:
                look = RIGHT
                dir = RIGHT
            elif event.key == SDLK_UP:
                dir = UP
            elif event.key == SDLK_DOWN:
                dir = DOWN
        elif event.type == SDL_KEYUP:
            running = False
            dir = IDLE


open_canvas(WIDTH, HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

quit = True
running = False
x, y = WIDTH // 2, HEIGHT // 2
look = LEFT
dir = IDLE
frame = 0

while quit:
    clear_canvas()
    tuk_ground.draw(WIDTH // 2, HEIGHT // 2)
    
    if running:
        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        if dir == LEFT:
            if not x < 0:
                x -= 10
        elif dir == RIGHT:
            if not x > WIDTH:
                x += 10
        elif dir == UP:
            if not y > HEIGHT:
                y += 10
        elif dir == DOWN:
            if not y < 0:
                y -= 10
        delay(0.05)
    else:
        character.clip_draw(frame * 100, 100 * (look + 2), 100, 100, x, y)
        delay(0.125)
        
    update_canvas()
    handle_events()
    
    frame = (frame + 1) % 8

close_canvas()
