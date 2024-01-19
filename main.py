import pygame
pygame.init() #initialisation pyagme
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Shooter game")

def draw_window():
    screen.fill("white")
    pygame.display.update()#

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()

if __name__ == "__main__":
    main()

pygame.quit()