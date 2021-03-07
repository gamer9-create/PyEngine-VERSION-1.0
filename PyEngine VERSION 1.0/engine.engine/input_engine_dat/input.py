from pygame import *
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *
from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *


class input_handler:
    def __init__(self, event):
        self.current_input = None
        self.event = event


    def mouse(self, v):
        if v == 1:
            if MOUSEBUTTONDOWN:
                return 0
        if v == 2:
            if MOUSEBUTTONUP:
                return 1


