import pygame
import time
from Boutons import *

pygame.init()

#créer la fenêtre du jeu :
ecran = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ultimate Archer")

#charger l'image de fond
image_fond = pygame.image.load("Images/Intro-fond.jpg").convert()
image_fond = pygame.transform.scale(image_fond, (1280, 720))

# Définir les polices
police_large = pygame.font.SysFont("arialblack", 60)
police_petite = pygame.font.SysFont("arialblack", 40)

def text(texte, police, couleur_texte, x, y):
    image_texte = police.render(texte, True, couleur_texte)
    ecran.blit(image_texte, (x, y))

run = True

#Boucle tant que la condition est vrai
while run :

    horloge = pygame.time.Clock()

    ecran.blit(image_fond, (0, 0))  # Fond d'écran
    text("ULTIMATE ARCHER", police_large, (255, 255, 255), 310, 120)
    text("Menu Principal", police_petite, (255, 255, 255), 470, 220)

    solo_button = create_buttons(550, 300, 150, 50, "Solo", (25, 4, 130), (0, 100, 200))
    solo_button.draw(ecran)
    one_vs_one_button = create_buttons(550, 400, 150, 50, "1v1",(179, 19, 18), (0, 100, 0))
    one_vs_one_button.draw(ecran)
    settings_button = create_buttons(500, 500, 260, 50, "Paramètres", (191, 207,231), (255, 140, 0))
    settings_button.draw(ecran)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()

