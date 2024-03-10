import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, health, max_health, velocity, image, x, y, weight, force):
        super().__init__()
        self.health = health
        self.max_health = max_health
        self.velocity = velocity
        self.image = pygame.image.load("Images/"+image)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.weight = weight
        self.force = force


humain = Player(4,4,15, "", 0,0,85, 30)
elf = Player(3, 3, 25, "", 0, 0, 60, 20)
orque = Player(7, 7, 5, "", 0, 0, 120, 50)


