import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from Boutons import Button
from Menus import *

pygame.init()

# Création de la fenêtre du jeu

"""mon_icone = '_'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(mon_icone)"""
SCREEN = pygame.display.set_mode((1280, 720))
icone = pygame.image.load("assets/icone.png")
pygame.display.set_caption("Ultimate Archer")
pygame.display.set_icon(icone)


# charger l'arrière plan
BG = pygame.image.load("assets/Background.png")




main_menu(SCREEN)
