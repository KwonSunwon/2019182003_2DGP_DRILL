from pico2d import *
import game_framework
import game_world

import random

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

PIXEL_PER_METER = 10.0 / 0.3
FLY_SPEED_KPH = 45
FLY_SPEED_MPM = FLY_SPEED_KPH * 1000.0 / 60.0
FLY_SPEED_MPS = FLY_SPEED_MPM / 60.0
FLY_SPEED_PPS = FLY_SPEED_MPS * PIXEL_PER_METER

CLIP_POSITION = ([0, 336], [183, 336], [367, 336], [550, 336], [734, 336],
                      [0, 168], [183, 168], [367, 168], [550, 168], [734, 168],
                      [0, 0], [183, 0], [367, 0], [550, 0])

class Bird:
    image = None
    
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
            
        self.x, self.y = random.randint(10, 1600 - 10), random.randint(250, 600 - 50)
        self.frame = random.randint(0, 7)
        
        self.dir = random.choice([-1, 1])
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        
        if (self.x <= 0 + 20 or self.x >= 1600 - 20): self.dir *= -1
    
    def draw(self):
        if self.dir == 1: # 왼쪽
            self.image.clip_draw(CLIP_POSITION[int(self.frame)][0], CLIP_POSITION[int(self.frame)][1], 179, 166, self.x, self.y, 110, 100)
        elif self.dir == -1:
            self.image.clip_composite_draw(CLIP_POSITION[int(self.frame)][0], CLIP_POSITION[int(self.frame)][1], 179, 166, 0,'h', self.x, self.y, 110, 100)
    
    