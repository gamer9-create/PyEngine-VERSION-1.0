import pygame
from camera import *
from game import *
from level_loader import *
from tile import *
from model import *
from replacements import *
from gravity import *

PyEngineInit()

window_size = (600, 600)

screen = PyEngineWindow(window_size[0], window_size[1])

cg = group()
tg = group()

myGameCamera = Camera(0,0,screen)
cg.add(myGameCamera)

myGameLevel = level(tg, myGameCamera)

GameObj = Game(myGameLevel, myGameCamera, tg, screen)
GameObj.window_width = window_size[0]
GameObj.window_height = window_size[1]
GameObj.window_title = PyEngineWindowTitleGet()

running = True

model = Model(0,0,pygame.Surface((40,40)),screen)
model2 = Model(0,60,pygame.Surface((40,40)), screen)
tg.add(model2)
tg.add(model)

camdx = 0
camdy = 0

myFPS = 0


while running:
    window_info = GameObj.events(pygame)
    event = window_info[1]
    myGameCamera.x = myGameCamera.x + camdx
    myGameCamera.y = myGameCamera.y + camdy
    myFPS = GameObj.getFPS()
    if event or window_info[0]:
        if window_info[0] == False:
            running = False
        if GameObj.isKeyDown(event):
            if GameObj.input(event, pygame.K_LEFT):
                camdx = 10
            if GameObj.input(event, pygame.K_RIGHT):
                camdx = -10
            if GameObj.input(event, pygame.K_UP):
                camdy = 10
            if GameObj.input(event, pygame.K_DOWN):
                camdy = -10
        if GameObj.isKeyUp(event):
            camdx = 0
            camdy = 0
    GameObj.setFPS(60)
    GameObj.update(pygame)









