
import pygame
import level_loader
import camera
import tile
import game
from replacements import *

pygame.init()


window_size = (800, 800)

screen = PyEngineWindow(window_size[0], window_size[1])
pygame.display.set_caption("Window")

running = True


tiles = []

camGroup = pygame.sprite.Group()

tile_group = pygame.sprite.Group()

camdx = 0
camdy = 0

myCamera = camera.Camera(0,0,screen)
myLevel = level_loader.level(tile_group, myCamera)
camGroup.add(myCamera)


Game = game.Game(myLevel, myCamera, tiles, screen)
Game.window_title = "Window"
Game.window_width = window_size[0]
Game.window_height = window_size[1]




while running:
    myCamera.x = myCamera.x + camdx
    myCamera.y = myCamera.y + camdy
    myCamera.rendering = True
    event_game = Game.events(pygame)
    info_list = event_game
    event = info_list[1]
    if event or info_list[1]:
        if info_list[0] == False:
            running = False
        if event.type == pygame.KEYDOWN:
            if Game.input(event,pygame.K_LEFT):
                camdx = camdx + 1
            if Game.input(event,pygame.K_RIGHT):
                camdx = camdx - 1
            if Game.input(event,pygame.K_UP):
                camdy = camdy + 1
            if Game.input(event,pygame.K_DOWN):
                camdy = camdy - 1
        if event.type == pygame.KEYUP:
            camdx = 0
            camdy = 0
    Game.update(pygame)
pygame.quit()

