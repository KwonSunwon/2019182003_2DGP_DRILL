from pico2d import *


# 이벤트 정의
RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD,
}


class AUTO_RUN:
    def enter(self, event):
        # print('ENTER AUTO_RUN')
        self.dir = self.face_dir
        pass
    
    def exit(self, event):
        # print('EXIT AUTO_RUN')
        pass
    
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x < 0:
            self.dir = 1
        elif self.x > 800:
            self.dir = -1
    
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 20, 150, 150)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 20, 150, 150)

class SLEEP:
    @staticmethod
    def enter(self, event):
        # print('ENTER SLEEP')
        self.dir = 0
    
    @staticmethod
    def exit(self, event):
        # print('EXIT SLEEP')
        pass
    
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
    
    @staticmethod
    def draw(self):
        if self.face_dir == 1: # 현재 오른쪽을 바라보고 있는 상태
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '',  self.x - 25, self.y - 25, 100, 100)


# 클래스를 이용해서 상태를 만듦
class IDLE:
    @staticmethod
    def enter(self, event):
        # print('ENTER IDLE')
        self.dir = 0
        # 타이머 설정
        self.timer = 1000
    
    @staticmethod
    def exit(self, event):
        # print('EXIT IDLE')
        pass
    
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: # 시간이 경과하면
            # 이벤트를 발생시켜줘야한다. 
            # self.q.insert(0, TIMER) # 객체지향 프로그래밍 위배, q를 직접 액세스하고 있음
            self.add_event(TIMER) # 객체지향적인 방법
    
    @staticmethod
    def draw(self):
        if self.face_dir == 1: # 현재 오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        
        

class RUN:
    def enter(self, event):
        # print('ENTER RUN')
        # self.dir 을 결정해야 함
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1
    
    def exit(self, event):
        # print('EXIT RUN')
        # run 을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다
        self.face_dir = self.dir
    
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
    
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)


next_state = {
    SLEEP: {RU: RUN, RD: RUN, LU: RUN, LD: RUN, SLEEP: SLEEP, AD: IDLE},
    IDLE: {RU: RUN, RD: RUN, LU: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN}, # 양쪽 방향키를 동시에 누르고 있는것도 고려해야함
    RUN: {RU: IDLE, RD: IDLE, LU: IDLE, LD: IDLE, AD: AUTO_RUN},
    AUTO_RUN: {RU: RUN, RD: RUN, LU: RUN, LD: RUN, AD: IDLE}
}


class Boy:
    
    def add_event(self, event):
        self.q.insert(0, event)
    
    def handle_event(self, event): # 소년이 스스로 이벤트를 처리할 수 있도록 만듦
        # event 는 키 이벤트, 이것을 내부 RD 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 추가
        
        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
    
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, event = None)

    def update(self):
        self.cur_state.do(self)
        
        if self.q: # 큐에 뭔가 들어있다면
            event = self.q.pop() # 이벤트를 가져오고
            self.cur_state.exit(self, event) # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] # 다음 상태를 계산하고
            self.cur_state.enter(self, event) # 다음 상태로 들어간다
        
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)