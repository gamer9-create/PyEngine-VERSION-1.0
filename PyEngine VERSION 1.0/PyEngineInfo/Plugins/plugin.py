

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


class Plugin:
    def __init__(self, data, plugin_program):
        self.data = data
        self.plugin_program = plugin_program
        
        
    def read_data(self):
        list = []
        for i in self.data:
            list.append(i)
        return list
    
    def write_data(self, data):
        self.data.append(data)

    def run(self):
        self.plugin_program.run()
