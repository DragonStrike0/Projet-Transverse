import pygame
import sys
import ctypes
import math
from projectile import Projectile
from tirs import Tir


class Player(pygame.sprite.Sprite):
    def __init__(self, health=4, max_health=4, velocity=15, image="humain.png", weight=85, force=30):
        super().__init__()
        self.health = health
        self.max_health = max_health
        self.velocity = velocity
        self.image = pygame.image.load("assets/player/"+image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 470
        self.weight = weight
        self.force = force

    def tir(self):
        projectile

    def move_right(self):
        self.rect.x += int(self.velocity/10)

    def move_left(self):
        self.rect.x -= int(self.velocity/10)


# les classes/ joueurs : temporaire
humain = Player(4, 4, 15, "humain.png", 85, 30)
elf = Player(3, 3, 25, "elf.png", 60, 20)
orc = Player(7, 7, 5, "orc.png", 120, 50)
