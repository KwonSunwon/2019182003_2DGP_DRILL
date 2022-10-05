from pico2d import *

WIDTH, HEIGHT = 1280, 1024
SPEED = 8
IDLE = 0
LEFT, RIGHT, UP, DOWN = 0b0001, 0b0010, 0b0100, 0b1000


def handle_events():
    global quit
    global running
    global dir
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
                dir |= LEFT
            elif event.key == SDLK_RIGHT:
                look = RIGHT
                dir |= RIGHT
            elif event.key == SDLK_UP:
                dir |= UP
            elif event.key == SDLK_DOWN:
                dir |= DOWN

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir &= ~LEFT
            elif event.key == SDLK_RIGHT:
                dir &= ~RIGHT
            elif event.key == SDLK_UP:
                dir &= ~UP
            elif event.key == SDLK_DOWN:
                dir &= ~DOWN
            if dir == IDLE:
                running = False


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
        character.clip_draw(frame * 100, 100 * (look - 1), 100, 100, x, y)
        if dir & LEFT == LEFT and look == LEFT:
            if not x < 0:
                x -= SPEED
        elif dir & RIGHT == RIGHT and look == RIGHT:
            if not x > WIDTH:
                x += SPEED
        if dir & UP == UP:
            if not y > HEIGHT:
                y += SPEED
        elif dir & DOWN == DOWN:
            if not y < 0:
                y -= SPEED
        delay(0.05)
    else:
        character.clip_draw(frame * 100, 100 * ((look - 1) + 2), 100, 100, x, y)
        delay(0.1)
        
    update_canvas()
    handle_events()
    
    frame = (frame + 1) % 8

close_canvas()
