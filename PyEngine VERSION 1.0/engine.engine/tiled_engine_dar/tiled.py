
import pygame
import os
import csv
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *

from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *
from PyEngine2.animation import *
from window_engine_dat.window import *

from input_engine_dat.input import *

from render_engine_dat.renderer import *


def read_csv(filename):
    map = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    return map


def read_tilemap(_map, TILE_SIZE, screen):
    map = _map
    print(map)
    read_map = []
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == "0":
                read_map.append(Model(x*TILE_SIZE,y*TILE_SIZE,pygame.Surface((TILE_SIZE,TILE_SIZE)), screen))
            x += 1
        y += 1
    return read_map



