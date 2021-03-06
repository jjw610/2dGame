
import game_framework
import prologue_state
import stage1_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('rsc\Title.png')
    global bgm
    bgm = load_music('sound\stitle.wav')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(prologue_state)
                #game_framework.change_state(stage1_state)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
