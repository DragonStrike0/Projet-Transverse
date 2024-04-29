import pygame
import sys
import ctypes
import math
from maps import Map
# from jeu import Game
# from arme import Arme


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, nom="flèche en bois", masse="0.2", image="flèche en bois.png", damage_multiplier="1"):
        super().__init__()
        self.nom = nom
        self.masses = masse
        self.image = pygame.image.load("assets/player/" + image)
        self.image = pygame.transform.scale(self.image, (1280 / 40, 1280 / 40))
        self.image = pygame.transform.rotate(self.image, -45)    # 180 - 45 pour les mechants
        self.damage = damage_multiplier
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 40
        self.rect.y = player.rect.y + 20

#    def move(self):
#       self.rect.x += self.