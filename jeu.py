import pygame
import sys
import ctypes
import math
from joueur import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}
