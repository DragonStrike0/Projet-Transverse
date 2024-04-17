import pygame
import sys
import ctypes
import math
from projectile import Projectile
from jeu import Game
from arme import Arme
from maps import Map


class Tir:

    def __init__(self, angle=45, gravite=Map().gravite, force=3 * Game().player.force - Arme().force_max,
                 poids=Projectile().poids, x_initial=Game().player.rect.x, y_initial=Game().player.rect.y):
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