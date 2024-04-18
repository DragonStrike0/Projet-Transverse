import pygame
import sys
import ctypes
import math


class Map(pygame.sprite.Sprite):

    def __init__(self,nom="prairie.jpg", dimensions_ecran=(1280, 720), gravite="9.8"):
        super().__init__()
        self.gravite = gravite
        self.image = pygame.image.load('assets/level/'+nom)
        level = pygame.image.load('assets/level/prairie.jpg')
        self.image = pygame.transform.scale(self.image, dimensions_ecran)
        level = pygame.transform.scale(level, (1280, 720))
        SCREEN = pygame.display.set_mode((1280, 720))


prairie = Map("prairie.jpg", (1280, 720), "9.8")