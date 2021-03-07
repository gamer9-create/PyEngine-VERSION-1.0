from pygame import *
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *
from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *


class Renderer:
    def __init__(self, window, rendering_size):
        self.rendering_surface = surface(rendering_size)
        self.rendering_surface.fill((255, 255, 255))
        self.window = window

    def render_frame(self):
        self.window.blit(self.rendering_surface, (0,0))

    def render(self, image, x, y):
        self.rendering_surface.blit(image, (x,y))





