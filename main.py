import pygame
pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ultimate Archer")

#define fonts
font = pygame.font.SysFont("arialblack", 40)
#define colours
TEXT_COL = (255, 255, 255)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def main():
    clock = pygame.time.Clock()
    # game loop
    run = True
    while run:

        screen.fill((52, 145, 91))
        pygame.display.update()
        clock.tick(60)
        draw_text("Lol",font,TEXT_COL,200,200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    main()

pygame.quit()