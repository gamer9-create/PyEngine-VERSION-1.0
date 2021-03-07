

import pygame
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *

from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *
from window_engine_dat.window import *

from input_engine_dat.input import *

from render_engine_dat.renderer import *
from tiled_engine_dar.tiled import *

PyEngineInit()
window_class = Window((800, 400), pygame.image.load("icon.png"), None)
screen = window_class.window_screen()
renderer = Renderer(screen,(800,400))
window_class.run()

objs = group()
tiles = group()



myCam = Camera(0,0,renderer.rendering_surface)
myCam.rendering = True
objs.add(myCam)

Level1 = level(tiles, myCam)
Level1.renderer = renderer
CURRENT_LEVEL = Level1

color_value = [194,194,194]
forever_x = 0
forever_y = 0

GameObj = Game(CURRENT_LEVEL, myCam, tiles, renderer.rendering_surface)
GameObj.window_title = PyEngineWindowTitleGet()
GameObj.window_width = 800
GameObj.window_height = 400
GameObj.icon = window_class.window_icon
GameObj.clearBG = True



running = True

while running:
    renderer.render_frame()
    myCam.x = myCam.x + forever_x
    myCam.y = myCam.y + forever_y
    #color_value[0] += 0.01
    #color_value[1] += 0.08
    #color_value[2] += 0.03
    if color_value[0] >= 195:
        color_value[0] = 0
    if color_value[1] >= 195:
        color_value[1] = 0
    if color_value[2] >= 195:
        color_value[2] = 0
    info_list = GameObj.events(pygame)
    event = info_list[1]
    should_close = info_list[0]
    if event or should_close:
        if should_close == False:
            running = False
        if GameObj.isKeyDown(event):
            if GameObj.input(event, pygame.K_LEFT):
                forever_x = -10
            if GameObj.input(event, pygame.K_RIGHT):
                forever_x = 10
            if GameObj.input(event, pygame.K_UP):
                forever_y = -10
            if GameObj.input(event, pygame.K_DOWN):
                forever_y = 10
        if GameObj.isKeyUp(event):
            forever_y = 0
            forever_x = 0
    GameObj.setFPS(60)
    GameObj.update(pygame)