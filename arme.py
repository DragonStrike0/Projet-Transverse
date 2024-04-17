import pygame
import sys
import ctypes
import math


class Arme(pygame.sprite.Sprite):

    def __init__(self, nom="arc long", projectile_type="fleches", image="arc_long.png", damage=2, poids=2,
                 force_max=50, precision=0):
        super().__init__()
        self.weight = poids
        self.force_max = force_max
        self.nom = nom
        self.ammo = projectile_type
        self.image = pygame.image.load("assets/player/" + image)
        self.rect = self.image.get_rect()
        # self.x = x
        # self.y = y
        self.damage = damage
        self.precision = precision


"""arc_long = Weapon("Arc Lourd", )"""


# potentiellement à supprimer car une classe similaire est dans projectile.py
"""class Arrow(pygame.sprite.Sprite):

    def __init__(self, nom, poids, image, damage):
        self.nom = nom
        self.poids = poids
        self.image = self.image.load("Image/"+image)
        self.damage = damage"""