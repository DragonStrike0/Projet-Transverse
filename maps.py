import pygame
import sys
import ctypes
import math


class Map(pygame.sprite.Sprite):

    def __init__(self, gravite="9.8"):
        super().__init__()
        self.gravite = gravite
