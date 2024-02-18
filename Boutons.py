import pygame

class Button:
    def __init__(self, x, y, width, height, text, font, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

    def perform_action(self):
        if self.action:
            self.action()

def solo_action():
    print("Mode Solo")

def one_vs_one_action():
    print("1v1 Mode")

def settings_action():
    print("Paramètres")

def return_to_menu_action():
    print("Retour au menu principal")

def create_buttons():
    # Définir les polices localement
    font_large = pygame.font.SysFont("arialblack", 40)
    font_small = pygame.font.SysFont("arialblack", 30)

    solo_button = Button(400, 500, 150, 50, "Solo", font_large, (0, 128, 255), (0, 100, 200), solo_action)
    one_vs_one_button = Button(640, 500, 150, 50, "1v1", font_large, (0, 128, 0), (0, 100, 0), one_vs_one_action)
    settings_button = Button(1000, 500, 200, 50, "Paramètres", font_small, (255, 165, 0), (255, 140, 0), settings_action)

    buttons = [solo_button, one_vs_one_button, settings_button]

    return buttons
