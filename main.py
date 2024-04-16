import pygame,sys,ctypes

from jeu import Game
from Boutons import Button

pygame.init()

# Création de la fenêtre du jeu

mon_icone = '_'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(mon_icone)
SCREEN = pygame.display.set_mode((1280, 720))
icone = pygame.image.load("assets/icone.png")
pygame.display.set_caption("Ultimate Archer")
pygame.display.set_icon(icone)

# charger l'arrière plan
BG = pygame.image.load("assets/Background.png")

# charger le jeu
game = Game()



def get_font(typo,size):
    if typo=='font':
        return pygame.font.Font("assets/font.ttf", size)
    elif typo=='Quest':
        return pygame.font.Font("assets/Quest.ttf", size)
    elif typo=='Text':
        return pygame.font.Font("assets/Text.ttf", size)
    elif typo=='Title':
        return pygame.font.Font("assets/Title.ttf", size)


# boucle active dans le menu après avoir cliqué sur "play"
def play():
    SCREEN.fill("black") #hors de la boucle pour éviter un bug graphique, remettre dans la boucle si nécessaire
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font('Title',45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 400),text_input="BACK", font=get_font('Text',75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_START = Button(image=None, pos=(640, 500), text_input="START", font=get_font('Text', 75), base_color="White",hovering_color="Green")

        PLAY_START.changeColor(PLAY_MOUSE_POS)
        PLAY_START.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_START.checkForInput(PLAY_MOUSE_POS):
                    start()

        pygame.display.update()

# boucle active dans le menu après avoir cliqué sur "options"
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font('Title',45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),text_input="BACK", font=get_font('Text',75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# boucle principale du menu
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font('Title',200).render("MAIN MENU", True, "#EB0000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/1V1 Rect.png"), pos=(640, 250),text_input="PLAY", font=get_font('Text',75), base_color="#A100FF", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),text_input="OPTIONS",font=get_font('Text',75), base_color="#A100FF", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),text_input="QUIT", font=get_font('Text',75), base_color="#A100FF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# boucle de partie/ boucle active après avoir cliqué sur "start" dans le menu play
def start():
    # paramètrage de l'affichage de la map, hors de la boucle pour éviter un bug graphique,
    # remettre dans la boucle si nécessaire
    level = pygame.image.load('assets/level/prairie.jpg')
    level = pygame.transform.scale(level, (1280, 720))
    SCREEN = pygame.display.set_mode((1280, 720))

    game.player.image = pygame.transform.scale(game.player.image, (1280 / 15, 1280 / 15))
    while True:
        # affichage de la map
        SCREEN.blit(level, (0, 0))

        # affichage du joueur
        SCREEN.blit(game.player.image, game.player.rect)

        # verifier les actions du joueur
        if game.pressed.get(pygame.K_d) or game.pressed.get(pygame.K_RIGHT):
            if game.player.rect.x < (SCREEN.get_width()-game.player.image.get_width()):
                game.player.move_right()
        elif game.pressed.get(pygame.K_q) or game.pressed.get(pygame.K_LEFT):
            if game.player.rect.x > 0:
                game.player.move_left()

        print(game.player.rect.x)


        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        # si le joueur ferme le jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # voir sur quelles touches le joueur appuis
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False


        pygame.display.update()



main_menu()