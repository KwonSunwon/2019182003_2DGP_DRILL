from pico2d import *

LEFT_WALL = 0
RIGHT_WALL = 800
BOTTOM = 100
ROPE_TOP = 380

open_canvas()

characterRenderInfo = {'frame': 0, 'x' : 0, 'y': 0, 'w': 128 , 'h': 120, 'cx': 0, 'cy': 0}
grassRenderInfo = {'cx': 400, 'cy': 30}
ropeRenderInfo = [
    {'x': 1696, 'y': 768, 'w': 64, 'h': 126, 'cx': 500, 'cy': 398},
    {'x': 52, 'y': 384, 'w': 24, 'h': 128, 'cx': 500, 'cy': 272},
    {'x': 820, 'y': 390, 'w': 24, 'h': 122, 'cx': 500, 'cy': 150},
]

character = load_image('char.png')
rope = load_image('char.png')
grass = load_image('grass.png')

def renderAll(characterRenderInfo):
    clear_canvas()
    grass.draw(grassRenderInfo['cx'], grassRenderInfo['cy'])
    for i in range(0, 3):
        rope.clip_draw(ropeRenderInfo[i]['x'], ropeRenderInfo[i]['y'], ropeRenderInfo[i]['w'], ropeRenderInfo[i]['h'], ropeRenderInfo[i]['cx'], ropeRenderInfo[i]['cy'])
    character.clip_draw(characterRenderInfo['frame'] * characterRenderInfo['w'] + characterRenderInfo['x'], characterRenderInfo['y'], characterRenderInfo['w'], characterRenderInfo['h'], characterRenderInfo['cx'], characterRenderInfo['cy'])
    update_canvas()
    delay(0.05)
    get_events()

def characterMove(startX, endX, isFormChanged):
    if isFormChanged:
        characterSlide(startX, endX)
    else:
        characterWalk(startX, endX)

def characterWalk(startX, endX):
    if startX < endX :
        gap = 10
        characterRenderInfo['x'] = 0
        characterRenderInfo['y'] = 1920
        frameCnt = 9
    else:
        gap = -10
        characterRenderInfo['x'] = 797
        characterRenderInfo['y'] = 1288
        frameCnt = 6
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = startX
    characterRenderInfo['cy'] = BOTTOM
    for cx in range(startX, endX + 1, gap):
        characterRenderInfo['frame'] = (characterRenderInfo['frame'] + 1) % frameCnt
        characterRenderInfo['cx'] = cx
        renderAll(characterRenderInfo)

def characterLookRope(cx):
    characterRenderInfo['frame'] = 0
    characterRenderInfo['x'] = 0
    characterRenderInfo['y'] = 904
    characterRenderInfo['cx'] = cx
    characterRenderInfo['cy'] = BOTTOM
    for frame in range(0, 7):
        characterRenderInfo['frame'] = frame
        renderAll(characterRenderInfo)
        renderAll(characterRenderInfo)

def characterHang(startY, endY):
    if startY < endY : gap = 5
    else : gap = -5
    characterRenderInfo['x'] = 0
    characterRenderInfo['y'] = 1158
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = 500
    characterRenderInfo['cy'] = startY
    for cy in range(startY, endY + 1, gap):
        characterRenderInfo['frame'] = (characterRenderInfo['frame'] + 1) % 6
        characterRenderInfo['cy'] = cy
        renderAll(characterRenderInfo)

def characterJump(startX):
    characterRenderInfo['x'] = 0
    characterRenderInfo['y'] = 775
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = startX
    characterRenderInfo['cy'] = BOTTOM
    for frame in range(0, 8):
        characterRenderInfo['frame'] = frame
        characterRenderInfo['cx'] += 10
        if frame < 4:
            characterRenderInfo['cy'] += 10
        else :
            characterRenderInfo['cy'] -= 10
        renderAll(characterRenderInfo)
    return characterRenderInfo['cx']

def characterDash(startX):
    characterRenderInfo['x'] = 0
    characterRenderInfo['y'] = 1418
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = startX
    characterRenderInfo['cy'] = BOTTOM + 10
    for frame in range(0, 7):
        characterRenderInfo['frame'] = frame
        if frame == 2:
            characterRenderInfo['cx'] += 10
        characterRenderInfo['cx'] += 20
        renderAll(characterRenderInfo)
    return characterRenderInfo['cx']

def characterFormChange(startX, isFormChanged):
    if not isFormChanged:
        characterRenderInfo['x'] = 0    
    else:
        characterRenderInfo['x'] = 265

    characterRenderInfo['y'] = 1800
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = startX
    characterRenderInfo['cy'] = BOTTOM
    for frame in range(0, 3):
        characterRenderInfo['frame'] = frame
        if frame is 1:
            renderAll(characterRenderInfo)
        renderAll(characterRenderInfo)
    return characterRenderInfo['cx'], not isFormChanged

def characterSlide(startX, endX):
    if startX < endX : gap = 10
    else : gap = -10
    characterRenderInfo['x'] = 650
    characterRenderInfo['y'] = 1800
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = startX
    characterRenderInfo['cy'] = BOTTOM
    for cx in range(startX, endX + 1, gap):
        characterRenderInfo['frame'] = (characterRenderInfo['frame'] + 1) % 7
        characterRenderInfo['cx'] = cx
        renderAll(characterRenderInfo)

def characterDead(cx):
    characterRenderInfo['x'] = 1295
    characterRenderInfo['y'] = 1038
    characterRenderInfo['frame'] = 0
    characterRenderInfo['cx'] = cx
    characterRenderInfo['cy'] = BOTTOM
    for frame in range(0, 3):
        characterRenderInfo['frame'] = frame
        renderAll(characterRenderInfo)
        renderAll(characterRenderInfo)
    characterRenderInfo['frame'] = 0
    characterRenderInfo['x'] = 1170
    characterRenderInfo['y'] = 1920
    characterRenderInfo['cy'] = BOTTOM - 5
    renderAll(characterRenderInfo)

while True:
    isFormChanged = False

    # walk and look rope, and climb rope
    characterMove(LEFT_WALL, 400, isFormChanged)
    characterLookRope(400)
    characterMove(400, 500, isFormChanged)
    characterHang(BOTTOM, ROPE_TOP)
    characterHang(ROPE_TOP, BOTTOM)
    characterMove(500, LEFT_WALL, isFormChanged)

    # jump
    characterMove(LEFT_WALL, 200, isFormChanged)
    cx = characterJump(200)
    characterMove(cx, cx + 100, isFormChanged)
    cx = characterJump(cx + 100)
    characterMove(cx, cx + 100, isFormChanged)

    # dash
    characterMove(LEFT_WALL, 200, isFormChanged)
    cx = characterDash(200)
    characterMove(cx, cx + 100, isFormChanged)
    cx = characterDash(cx + 100)
    characterMove(cx, cx + 100, isFormChanged)

    # form change and walk(or slide)
    characterMove(LEFT_WALL, 100, isFormChanged)
    cx, isFormChanged = characterFormChange(100, isFormChanged)
    characterMove(cx, cx + 300, isFormChanged)
    cx, isFormChanged = characterFormChange(cx + 300, isFormChanged)
    characterMove(cx, cx + 100, isFormChanged)

    # dead
    characterDead(400)

close_canvas()
