import pygame
import sys
import ctypes
import math
from jeu import Game
from arme import Arme


class Projectile(pygame.sprite.Sprite):

    def __init__(self, nom="flèche en bois", poids="0.2", image="flèche en bois.png", damage_multiplier="1"):
        super().__init__()
        self.nom = nom
        self.poids = poids
        self.image = pygame.image.load("assets/player/" + image)
        self.damage = damage_multiplier
        self.rect = self.image.get_rect()
