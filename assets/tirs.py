import pygame
import sys
import ctypes
import math
from projectile import Projectile
from Jeu import Game
from arme import Arme
# from maps import Map


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

angle = angle_entre_droite_et_abscisse(x1, y1, x2, y2)
print("L'angle entre la droite et l'axe des abscisses est :", angle, "degrés.")

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


"""
# Paramètres de la simulation
temps_ecoule = 0  # en secondes
increment_temps = 0.01  # incrément du temps en secondes


# Boucle principale
while True:

    # Calculer la position du projectile en fonction du temps
    x = vitesse_x * temps_ecoule
    y = hauteur - (vitesse_y * temps_ecoule - 0.5 * gravite * temps_ecoule**2)

    # Dessiner le projectile (un simple cercle)
    pygame.draw.circle(fenetre, NOIR, (int(x), int(y)), 5)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Mettre à jour le temps écoulé
    temps_ecoule += increment_temps"""