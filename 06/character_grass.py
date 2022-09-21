from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def drawRectangle():
    x = 400
    y = 90
    while (True):
        clear_canvas_now()
        grass.draw_now(400, 30)
        
        character.draw_now(x, y)
        if(x < 780 and y == 90):
            x += 2
        elif(x == 780 and y < 550):
            y += 2
        elif(x > 20 and y == 550):
            x -= 2
        elif(x == 20 and y > 90):
            y -= 2
            
        delay(0.01)
        if (x == 400 and y == 90):
            break

def drawCircle():
    x = 400
    y = 90
    angle = 180
    while(True):
        clear_canvas_now()
        grass.draw_now(400, 30)
        
        character.draw_now(x, y)
        x = math.sin(angle / 360 * 2 * math.pi) * 200 + 400
        y = math.cos(angle / 360 * 2 * math.pi) * 200 + 285
        angle += 1
        if(angle == 360):
            angle = 0;
        
        delay(0.01)
        if(angle == 180):
            break
    
while(1):
    drawRectangle()
    drawCircle()

close_canvas()
