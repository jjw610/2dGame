import random

from pico2d import *
import game_framework
import ending_state
from human import Human
from enemy import Skeleton, Ghost
from collide import collide
name = "MainState"


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


def enter():
    global bf
    global human
    global skeleton
    global ghost
    global background
    global box1, box2, box3, box4,box5
    human = Human(50, 500)
    skeleton = Skeleton(700, 500)
    ghost = Ghost(400, 300)
    background = BackGround()
    box1 = Object(3, 146, 408)
    box2 = Object(0, 182, 192)
    box3 = Object(1, 400, 300)
    box4 = Object(4, 474, 148)
    box5 = Object(0, 506, 456)

def exit():
    global human, skeleton, ghost
    global background
    global box1, box2, box3, box4, box5
    del (human)
    del (skeleton)
    del (ghost)
    del (background)
    del (box1)
    del (box2)
    del (box3)
    del (box4)
    del (box5)

def pause():
    pass


def resume():
    pass

def handle_events():
    global human
    global box1, box2, box3, box4, box5
    events = get_events()
    skeleton.handle_event()
    ghost.handle_event()
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
    elif collide(human, box3):
        human.collideobject = collide(human, box3)
    elif collide(human, box4):
        human.collideobject = collide(human, box4)
    elif collide(human, box5):
        human.collideobject = collide(human, box5)
    elif collide(human, skeleton):
        game_framework.change_state(ending_state)
    elif collide(human, ghost):
        game_framework.change_state(ending_state)


    # if collide(skeleton, box1):
    #     skeleton.collideobject = collide(skeleton, box1)
    # elif collide(skeleton, box2):
    #     skeleton.collideobject = collide(skeleton, box2)
    # elif collide(skeleton, box3):
    #     skeleton.collideobject = collide(skeleton, box3)
    # elif collide(skeleton, box4):
    #     skeleton.collideobject = collide(skeleton, box4)

def update():
    human.update()
    skeleton.update()
    ghost.update()
    delay(0.03)


def draw():
    clear_canvas()
    background.draw()
    box1.draw()
    box2.draw()
    box3.draw()
    box4.draw()
    box5.draw()
    human.draw()
    skeleton.draw()
    ghost.draw()


    human.draw_bb()
    box1.draw_bb()
    box2.draw_bb()
    box3.draw_bb()
    box4.draw_bb()
    box5.draw_bb()
    skeleton.draw_bb()
    ghost.draw_bb()


    update_canvas()








