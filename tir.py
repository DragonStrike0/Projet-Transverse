import pygame
import sys
import ctypes
import math
from maps import Map
from jeu import Game
from tir import Arme


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


class Arme(pygame.sprite.Sprite):

    def __init__(self, nom="arc long", projectile_type="fleches", image="arc long.png", damage=2, poids=2,
                 force_max=50, precision=0):
        super().__init__()
        self.weight = poids
        self.force_max = force_max
        self.nom = nom
        self.ammo = projectile_type
        self.image = pygame.image.load("assets/player/" + image)
        self.image = pygame.transform.scale(self.image, (1280 / 22, 1280 / 22))
        self.image = pygame.transform.rotate(self.image, 180 + 45)  # 45 pour les mechants
        self.rect = self.image.get_rect()
        self.damage = damage
        self.precision = precision



def calculer_pente(x1, y1, x2, y2):
    if (x2 - x1 == 0):
        return False, 0
    return True, (y2 - y1) / (x2 - x1)


def calculer_angle(pente):
    return math.degrees(math.atan(pente))


def angle_entre_droite_et_abscisse(x1, y1, x2, y2):
    pente = calculer_pente(x1, y1, x2, y2)
    if pente[0]:
        angle = calculer_angle(pente[1])
    else:
        if y2 < y1:
            angle = -90
        else:
            angle = 90

    return angle


# Exemple d'utilisation
x1, y1 = 0, 0
x2, y2 = -10, 0
class Tir:

    def __init__(self, angle=angle_entre_droite_et_abscisse(x1, y1, x2, y2), gravite=Game.map().gravite,
                 force=3 * Game().player.force - Arme().force_max, poids=Projectile().masses,
                 x_initial=Game().player.rect.x, y_initial=Game().player.rect.y):
        self.vitesse_initiale = 100 / force
        self.angle_rad = angle * (math.pi / 180)
        self.vitesse_x = self.vitesse_initiale * math.cos(self.angle_rad)
        self.vitesse_y = self.vitesse_initiale * math.sin(self.angle_rad)
        self.x_initial = x_initial
        self.y_initial = y_initial

def calculer_pente(x1, y1, x2, y2):
    if (x2 - x1 == 0):
        return False, 0
    return True, (y2 - y1) / (x2 - x1)


def calculer_angle(pente):
    return math.degrees(math.atan(pente))


def angle_entre_droite_et_abscisse(x1, y1, x2, y2):
    pente = calculer_pente(x1, y1, x2, y2)
    if pente[0]:
        angle = calculer_angle(pente[1])
    else:
        if y2 < y1:
            angle = -90
        else:
            angle = 90

    return angle
