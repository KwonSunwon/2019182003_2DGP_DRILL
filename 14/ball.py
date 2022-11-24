import random
from pico2d import *
import game_world

import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(10, server.background.w - 10), random.randint(10, server.background.h - 10)

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass
    
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        # print('ball disappear')
        if group == 'boy:ball':
            game_world.remove_object(self)
    
    def stop(self):
        self.fall_speed = 0