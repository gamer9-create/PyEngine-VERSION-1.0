

import pygame
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


class Program:
    def __init__(self):
        self.custom_app = None
        # set whatever variables you want


    def run(self):
        self.custom_app.run() # Make this function run the app

