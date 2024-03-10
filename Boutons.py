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

def create_buttons(x, y, width, height, text, color, hover_color, ):
    # Définir les polices localement
    font_large = pygame.font.SysFont("arialblack", 40)
    boutons = Button(x, y, width, height, text, font_large, color, hover_color, action=None)
    return boutons
