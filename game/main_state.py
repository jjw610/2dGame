import random
import json
import os
from pico2d import *
import game_framework
import title_state

name = "MainState"

class Human:
    RIGHT_RUN, DOWN_RUN, LEFT_RUN, UP_RUN, RIGHT_STAND, DOWN_STAND, LEFT_STAND, UP_STAND = 0, 1, 2, 3, 4, 5, 6, 7
    collideobject = 0
    def get_bb(self):
        return self.x - 10, self.y - 35, self.x + 12, self.y-25

    def get_xy(self):
        return self.x, self.y;

    def get_st(self):
        return self.state

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def __init__(self, x, y ):
        self.state = 4
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('image\character\human.png')


    def update(self):

        self.frame = (self.frame + 1) % 9
        if self.collideobject == 0:
            if self.state in (self.RIGHT_RUN,):
                self.x = min(764, self.x + 4)
            elif self.state in (self.LEFT_RUN,):
                self.x = max(32, self.x - 4)
            if self.state in (self.UP_RUN, ):
                self.y = min(556, self.y + 4)
            elif self.state in (self.DOWN_RUN, ):
                self.y = max(40, self.y - 4)
        else:
            if self.state in (self.RIGHT_RUN,):
                if self.collideobject != 1:
                    self.x = min(764, self.x + 4)
            elif self.state in (self.LEFT_RUN,):
                if self.collideobject != 3:
                    self.x = max(32, self.x - 4)
            if self.state in (self.UP_RUN, ):
                if self.collideobject != 4:
                    self.y = min(556, self.y + 4)
            elif self.state in (self.DOWN_RUN, ):
                if self.collideobject != 2:
                    self.y = max(40, self.y - 4)
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if self.state in (self.DOWN_RUN, self.LEFT_RUN, self.UP_RUN, self.DOWN_STAND, self.UP_STAND, self.RIGHT_STAND, self.LEFT_STAND):
                    self.state = 0
            elif event.key == SDLK_DOWN:
                if self.state in (self.LEFT_RUN, self.UP_RUN, self.RIGHT_RUN,self.DOWN_STAND, self.UP_STAND, self.RIGHT_STAND, self.LEFT_STAND):
                    human.state = 1
            elif event.key == SDLK_LEFT:
                if human.state in (human.DOWN_RUN, human.UP_RUN, human.RIGHT_RUN, human.DOWN_STAND, human.UP_STAND,human.RIGHT_STAND, human.LEFT_STAND):
                    human.state = 2
            elif event.key == SDLK_UP:
                if human.state in (human.DOWN_RUN, human.LEFT_RUN, human.RIGHT_RUN, human.DOWN_STAND, human.UP_STAND,human.RIGHT_STAND, human.LEFT_STAND):
                    human.state = 3
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if human.state == human.RIGHT_RUN:
                    human.state = 4
                elif human.state == human.UP_RUN:
                    human.state = human.UP_RUN
                elif human.state == human.LEFT_RUN:
                    human.state = human.LEFT_RUN
                elif human.state == human.DOWN_RUN:
                    human.state = human.DOWN_RUN
            elif event.key == SDLK_DOWN:
                if human.state == human.DOWN_RUN:
                    human.state = 5
                elif human.state == human.UP_RUN:
                    human.state = human.UP_RUN
                elif human.state == human.LEFT_RUN:
                    human.state = human.LEFT_RUN
                elif human.state == human.RIGHT_RUN:
                    human.state = human.RIGHT_RUN
            elif event.key == SDLK_LEFT:
                if human.state == human.LEFT_RUN:
                    human.state = 6
                elif human.state == human.UP_RUN:
                    human.state = human.UP_RUN
                elif human.state == human.RIGHT_RUN:
                    human.state = human.RIGHT_RUN
                elif human.state == human.DOWN_RUN:
                    human.state = human.DOWN_RUN
            elif event.key == SDLK_UP:
                if human.state == human.UP_RUN:
                    human.state = 7
                elif human.state == human.RIGHT_RUN:
                    human.state = human.RIGHT_RUN
                elif human.state == human.LEFT_RUN:
                    human.state = human.LEFT_RUN
                elif human.state == human.DOWN_RUN:
                    human.state = human.DOWN_RUN
    def draw(self):
        if self.state < 4:
            self.image.clip_draw(self.frame * 64, (self.state * 64) - 1, 64, 64, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 0, ((self.state-4) * 64) - 1, 64, 64, self.x, self.y)

#---------------------------------------------------------------------------------------------------------------
class Skeleton:
    RIGHT_RUN, DOWN_RUN, LEFT_RUN, UP_RUN, RIGHT_STAND, DOWN_STAND, LEFT_STAND, UP_STAND = 0, 1, 2, 3, 4, 5, 6, 7
    collideobject = 0
    def get_bb(self):
        return self.x - 10, self.y - 35, self.x + 12, self.y-25

    def get_xy(self):
        return self.x, self.y;

    def get_st(self):
        return self.state

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def __init__(self, x, y ):
        self.nowst = 0
        self.runtime = 0
        self.state = 4
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('image\character\skeleton.png')


    def update(self):

        self.frame = (self.frame + 1) % 9
        if self.collideobject == 0:
            if self.state in (self.RIGHT_RUN,):
                self.x = min(764, self.x + 4)
            elif self.state in (self.LEFT_RUN,):
                self.x = max(32, self.x - 4)
            if self.state in (self.UP_RUN, ):
                self.y = min(556, self.y + 4)
            elif self.state in (self.DOWN_RUN, ):
                self.y = max(40, self.y - 4)
        else:
            if self.state in (self.RIGHT_RUN,):
                if self.collideobject != 1:
                    self.x = min(764, self.x + 4)
            elif self.state in (self.LEFT_RUN,):
                if self.collideobject != 3:
                    self.x = max(32, self.x - 4)
            if self.state in (self.UP_RUN, ):
                if self.collideobject != 4:
                    self.y = min(556, self.y + 4)
            elif self.state in (self.DOWN_RUN, ):
                if self.collideobject != 2:
                    self.y = max(40, self.y - 4)
    def handle_event(self):
        self.runtime = self.runtime + 1
        if(self.runtime == 20):
            self.nowst = random.randint(0, 3)
        elif(self.runtime == 40):
            self.nowst = self.nowst +4
        elif (self.runtime == 60):
            self.runtime = 0
        self.state = self.nowst
    def draw(self):
        if self.state < 4:
            self.image.clip_draw(self.frame * 64, (self.state * 64) - 1, 64, 64, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 0, ((self.state-4) * 64) - 1, 64, 64, self.x, self.y)

class BackGround:
    def __init__(self):
        self.image = load_image('image\ground\state1-1.png')

    def draw(self):
        self.image.draw(400, 300)
class Object():



    def __init__(self, type, x, y):
        self.obn = type
        self.col = 0
        self.x, self.y = x, y
        if self.obn == 0:
            self.image = load_image('image\object\oox1-1.png')
            self.xx = 18
            self.yy = 22
        elif self.obn == 1:
            self.image = load_image('image\object\oox2-1.png')
            self.xx = 31
            self.yy = 37
        elif self.obn == 2:
            self.image = load_image('image\object\itable1-1.png')
            self.xx = 42
            self.yy = 30
        elif self.obn == 3:
            self.image = load_image('image\object\itable2-1.png')
            self.xx = 42
            self.yy = 30
        elif self.obn == 4:
            self.image = load_image('image\object\itable3-1.png')
            self.xx = 42
            self.yy = 30

    def get_bb(self):
        return self.x - self.xx, self.y - self.yy, self.x + self.xx, self.y + self.yy

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_xy(self):
        return self.x, self.y;

    def draw(self):
        self.image.draw(self.x,self.y)

def collide(a, b):
    global bf
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    stt = a.get_st()

    if left_a > right_b:
        b.col = 0
        a.collideobject = 0
        return False
    elif right_a < left_b:
        b.col = 0
        a.collideobject = 0
        return False
    elif top_a < bottom_b:
        b.col = 0
        a.collideobject = 0
        return False
    elif bottom_a > top_b:
        b.col = 0
        a.collideobject = 0
        return False

    if stt in (a.RIGHT_RUN, a.RIGHT_STAND):
        if b.col == 0:
            b.col = 1
            bf = 1
            return bf
        else:
            return bf
    elif stt in (a.DOWN_RUN, a.DOWN_STAND):
        if b.col == 0:
            b.col = 1
            bf = 2
            return bf
        else:
            return bf
    elif stt in (a.LEFT_RUN, a.LEFT_STAND):
        if b.col == 0:
            b.col = 1
            bf = 3
            return bf
        else:
            return bf
    elif stt in (a.UP_RUN, a.UP_STAND):
        if b.col == 0:
            b.col = 1
            bf = 4
            return bf
        else:
            return bf

    return False

def enter():
    global bf
    global human
    global skeleton
    global background
    global box1, box2
    human = Human(50, 500)
    skeleton = Skeleton(300, 500)
    background = BackGround()
    box1 = Object(0, 400,300 )
    box2 = Object(0, 300, 200)
def exit():
    global human
    global skeleton
    global background
    global box1, box2
    del (human)
    del (skeleton)
    del (background)
    del (box1)
    del (box2)
def pause():
    pass


def resume():
    pass


def handle_events():
    global human
    global box1, box2
    events = get_events()
    skeleton.handle_event()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pass
        human.handle_event(event)


    if collide(human, box1):
        human.collideobject = collide(human, box1)
    elif collide(human, box2):
        human.collideobject = collide(human, box2)

def update():
    human.update()
    skeleton.update()
    delay(0.03)


def draw():
    clear_canvas()
    background.draw()
    box1.draw()
    box2.draw()
    human.draw()
    skeleton.draw()


    human.draw_bb()
    box1.draw_bb()
    box2.draw_bb()
    skeleton.draw()

    update_canvas()








