import pygame
import sys
import ctypes
import math
from tir import Projectile
from tir import Arme


class Player(pygame.sprite.Sprite):
    def __init__(self, health=4, max_health=4, velocity=1, image="humain.png", weight=85, force=30, arme=Arme()):
        super().__init__()
        self.health = health
        self.max_health = max_health
        self.velocity = velocity
        self.image = pygame.image.load("assets/player/"+image)
        self.image = pygame.transform.scale(self.image, (1280 / 15, 1280 / 15))
        self.image = pygame.transform.flip(self.image, False, False)   # True, False pour les mechants
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 470
        self.weight = weight
        self.force = force
        self.arme = arme
        self.arme.rect.x = 100 + 16
        self.arme.rect.y = 470
        self.all_projectiles = pygame.sprite.Group()

    def tirer(self):
        self.all_projectiles.add(Projectile(self))

    # la vitesse ne change pas comme voulu car le perso se déplace en pixel (je crois) et que c'est pas assez précis,
    # je sais pas comment faire mais au pire osef je verrai plus tard
    def move_right(self):
        self.rect.x += (10 + self.velocity)/10
        self.arme.rect.x += (10 + self.velocity)/10

    def move_left(self):
        self.rect.x -= (10 + self.velocity)/10
        self.arme.rect.x -= (10 + self.velocity)/10


# les classes/ joueurs : temporaire
humain = Player(4, 4, 2, "humain.png", 85, 30)
elf = Player(3, 3, 3, "elf.png", 60, 20)
orc = Player(7, 7, 1, "orc.png", 120, 50)
