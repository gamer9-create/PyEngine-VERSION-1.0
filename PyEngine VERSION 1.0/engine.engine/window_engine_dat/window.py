from pygame import *
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *
from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *


class Window:
    def __init__(self, window_size, window_icon, window_title):
        self.window_size = window_size
        self.window_icon = window_icon
        self.window_title = window_title
        self.screen = None
    def window_screen(self):
        s = PyEngineWindow(self.window_size[0], self.window_size[1])
        self.screen = s
        return s
    def run(self):
        if self.screen:
            if self.window_title:
                PyEngineWindowTitleSet(self.window_title)
            if self.window_icon:
                PyEngineWindowIconSet(self.window_icon)





