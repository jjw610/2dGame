import random
import json
import os
from pico2d import *
import game_framework
import title_state

name = "MainState"

class Human:
    RIGHT_RUN, DOWN_RUN, LEFT_RUN, UP_RUN, RIGHT_STAND, DOWN_STAND, LEFT_STAND, UP_STAND = 0, 1, 2, 3, 4, 5, 6, 7
    def handle_left_run(self):
        if self.x > 0:
            self.x -= 6
    def handle_left_stand(self):
        pass
    def handle_right_run(self):
        if self.x < 800:
            self.x += 6
    def handle_right_stand(self):
        pass
    def handle_up_run(self):
        if self.y < 800:
            self.y += 6
    def handle_up_stand(self):
        pass
    def handle_down_run(self):
        if self.y > 0:
            self.y -= 6
    def handle_down_stand(self):
        pass

    handle_state = {
        RIGHT_RUN: handle_right_run,
        DOWN_RUN: handle_down_run,
        LEFT_RUN: handle_left_run,
        UP_RUN: handle_up_run,
        RIGHT_STAND: handle_right_stand,
        DOWN_STAND: handle_down_stand,
        LEFT_STAND: handle_left_stand,
        UP_STAND: handle_left_stand
    }

    def __init__(self):
        self.state = 4
        self.x, self.y = 400, 300
        self.frame = 0
        self.image = load_image('image\character\human.png')
        self.dir = 4

    def update(self):
        self.frame = (self.frame + 1) % 9
        self.handle_state[self.state](self)
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if human.state in (human.DOWN_RUN, human.LEFT_RUN, human.UP_RUN, human.DOWN_STAND, human.UP_STAND, human.RIGHT_STAND, human.LEFT_STAND):
                    human.state = 0
            elif event.key == SDLK_DOWN:
                if human.state in (human.LEFT_RUN, human.UP_RUN, human.RIGHT_RUN, human.DOWN_STAND, human.UP_STAND, human.RIGHT_STAND, human.LEFT_STAND):
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

class BackGround:
    def __init__(self):
        self.image = load_image('image\ground\state1-1.png')

    def draw(self):
        self.image.draw(400, 300)
class Object():
    def __init__(self):
        self.obn = 0
        self.x, self.y = 400, 300
        if self.obn == 0:
            self.image = load_image('image\object\oox1-1.png')
        elif self.obn == 1:
            self.image = load_image('image\object\oox2-1.png')
        elif self.obn == 2:
            self.image = load_image('image\object\itable1-1.png')
        elif self.obn == 3:
            self.image = load_image('image\object\itable3-1.png')


    def draw(self):
        self.image.draw(400, 300)



def enter():
    global human
    global background
    global box
    human = Human()
    background = BackGround()
    box = Object()
def exit():
    global human
    global background
    global box
    del (human)
    del (background)
    del (box)

def pause():
    pass


def resume():
    pass


def handle_events():
    global human
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            human.handle_event(event)
            pass

def update():
    human.update()
    delay(0.05)
def draw():
    clear_canvas()
    background.draw()
    box.draw()
    human.draw()
    update_canvas()





