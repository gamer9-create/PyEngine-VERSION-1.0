import pygame
from PyEngine2.game import *
from PyEngine2.tile import *
from PyEngine2.camera import *
from PyEngine2.model import *
from PyEngine2.level_loader import *
from PyEngine2.replacements import *

PyEngineInit()

class AnimationHandler:
    def __init__(self, images, sprite, speed, images_count):
        self.sprite = sprite
        self.images = images
        self.speed = speed
        self.animation_num = 0
        self.images_count = images_count

    def animate(self):
        self.animation_num = self.animation_num + self.speed
        if self.animation_num >= self.images_count-1:
            self.animation_num = 0
        self.sprite.image = self.images[int(self.animation_num)]






