from pico2d import *

characterRenderInfo = {'status': False, 'frame': 0, 'y': 0, 'w': 0, 'h': 0, 'cx': 0, 'cy': 0}
objectRenderInfo = {'status': False, 'frame': 0, 'y': 0, 'w': 0, 'h': 0, 'cx': 0, 'cy': 0}

character = load_image('sonic.png')
object = load_image('bomb.png')

def renderAll(characterRenderInfo, objectRenderInfo):
    clear_canvas()
    if characterRenderInfo['status'] == True:
        character.clip_draw(characterRenderInfo['frame'] * characterRenderInfo['w'], 0, characterRenderInfo['w'], characterRenderInfo['h'], characterRenderInfo['x'], characterRenderInfo['y'])
    if objectRenderInfo['status'] == True:
        object.clip_draw(objectRenderInfo['frame'] * objectRenderInfo['w'], 0, objectRenderInfo['w'], objectRenderInfo['h'], objectRenderInfo['x'], objectRenderInfo['y'])
    update_canvas()
    delay(0.01)
    get_events()

def characterIdle():
    characterRenderInfo['status'] = True
    characterRenderInfo['frame'] = 0
    characterRenderInfo['y'] = 968
    characterRenderInfo['w'] = 80
    characterRenderInfo['h'] = 120
    characterRenderInfo['x'] = 400
    characterRenderInfo['y'] = 300
    for i in range(0, 6 + 1):
        characterRenderInfo['frame'] = i
        renderAll(characterRenderInfo, objectRenderInfo)

def characterWalk():
    pass

def characterRun():
    pass

def characterKick():
    pass

def characterSpin():
    pass

def characterDie():
    pass

def objectBomb():
    pass

open_canvas()

while True:
    characterIdle()

close_canvas()

