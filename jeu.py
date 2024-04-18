import pygame
import sys
import ctypes
import math
from joueur import Player
from maps import Map
# from projectile import Projectile
# from arme import Arme


class Game:

    def __init__(self):
        self.player = Player()
        self.map = Map()
        self.pressed = {}
