import random

from pico2d import *
import game_framework
import ending_state
import second_state
from human import Human
from enemy import Skeleton, Ghost
from collide import collide, raidecollide, collidee
from nextspot import NextSpot
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
    global nextspot
    human = Human(50, 500)
    skeleton = Skeleton(700, 500)
    ghost = Ghost(400, 300)
    background = BackGround()
    box1 = Object(3, 306, 488)
    box2 = Object(0, 182, 192)
    box3 = Object(1, 400, 300)
    box4 = Object(4, 474, 148)
    box5 = Object(0, 506, 456)
    nextspot = NextSpot(660, 20)
    global bgm
    bgm = load_music('sound\snormal.wav')
    bgm.set_volume(64)
    bgm.repeat_play()
    global bgm2
    bgm2 = load_music('sound\sfollow.wav')
    bgm2.set_volume(64)
    global c
    global bgmswt
    bgmswt = 0
    c = 0

def exit():
    global human, skeleton, ghost
    global background
    global box1, box2, box3, box4, box5
    global nextspot
    del (human)
    del (skeleton)
    del (ghost)
    del (background)
    del (box1)
    del (box2)
    del (box3)
    del (box4)
    del (box5)
    del (nextspot)

def pause():
    pass


def resume():
    pass

def handle_events():
    global c
    global bgmswt
    global human
    global box1, box2, box3, box4, box5
    global nextspot
    events = get_events()
    skeleton.handle_event(human)
    ghost.handle_event(human)
    if c == 1:
        if bgmswt == 0:
            bgmswt = 1
            bgm.stop()
            bgm2.repeat_play()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pass
        human.handle_event(event)

    if collidee(skeleton, box1):
        skeleton.collideobject = collidee(skeleton, box1)
    elif collidee(skeleton, box2):
        skeleton.collideobject = collidee(skeleton, box2)
    elif collidee(skeleton, box3):
        skeleton.collideobject = collidee(skeleton, box3)
    elif collidee(skeleton, box4):
        skeleton.collideobject = collidee(skeleton, box4)
    elif collidee(skeleton, box5):
        skeleton.collideobject = collidee(skeleton, box5)
    if raidecollide(human, skeleton):
        if c == 0:
            c = 1
        skeleton.attack = raidecollide(human, skeleton)

    if raidecollide(human, ghost):
        ghost.attack = raidecollide(human, ghost)





    if collide(human, box1):
        human.col = collide(human, box1)
    elif collide(human, box2):
        human.col = collide(human, box2)
    elif collide(human, box3):
        human.col = collide(human, box3)
    elif collide(human, box4):
        human.col = collide(human, box4)
    elif collide(human, box5):
        human.col = collide(human, box5)
    elif collide(human, skeleton):
        game_framework.change_state(ending_state)
    elif collide(human, ghost):
        game_framework.change_state(ending_state)
    elif collide(human, nextspot):
        game_framework.change_state(second_state)



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
    skeleton.update(human)
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
    skeleton.draw_raider()
    ghost.draw_bb()
    ghost.draw_raider()
    nextspot.draw_bb()



    update_canvas()








