import pygame
import time
from Boutons import*

pygame.init()

# Créer la fenêtre de jeu
LARGEUR_ECRAN = 1280
HAUTEUR_ECRAN = 720

ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("Ultimate Archer")

# Charger l'image de fond
image_fond = pygame.image.load("Images\Intro-fond.jpg").convert()
image_fond = pygame.transform.scale(image_fond, (LARGEUR_ECRAN, HAUTEUR_ECRAN))

# Définir les polices
police_large = pygame.font.SysFont("arialblack", 60)
police_petite = pygame.font.SysFont("arialblack", 40)
# Définir les couleurs
COULEUR_TEXTE = (255, 255, 255)

def text(texte, police, couleur_texte, x, y):
    image_texte = police.render(texte, True, couleur_texte)
    ecran.blit(image_texte, (x, y))

def main():

    horloge = pygame.time.Clock()
    run = True
    buttons = create_buttons()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_hovered(pygame.mouse.get_pos()):
                        button.perform_action()

        horloge.tick(60)
        #Intro
        ecran.blit(image_fond, (0, 0))  #Fond d'écran
        text("ULTIMATE ARCHER", police_large, COULEUR_TEXTE, 310, 120)
        text("Menu Principal", police_petite, COULEUR_TEXTE, 470, 220)
        for button in buttons:
            button.draw(ecran)

        pygame.display.update()

if __name__ == "__main__":
    main()

pygame.quit()
