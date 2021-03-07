import pygame
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *
from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *
from PyEngine2.animation import *

PyEngineInit()

class PhysicsHandler:
    def __init__(self, sprite, other_objs):
        self.sprite = sprite
        self.objs = other_objs

    def physics(self):
        for i in self.objs:
            if not i == self:
                if i.rect.colliderect(self.sprite.rect):
                    return False
                else:
                    return True
