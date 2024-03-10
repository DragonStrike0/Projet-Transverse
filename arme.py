import pygame

class Weapon(pygame.sprite.Sprite):

    def __init__(self, nom, arrow_type, image, damage):
        self.weight = 2
        self.f_max = 50
        self.nom = nom
        self.ammo = arrow_type
        self.image = self.image.load("Image/"+image)
        self.damage = damage
        self.precision = 0

"""arc_long = Weapon("Arc Lourd", )"""


class Arrow(pygame.sprite.Sprite):

    def __init__(self, nom, poid, image, damage):
        self.nom = nom
        self.poid = poid
        self.image = self.image.load("Image/"+image)
        self.damage = damage