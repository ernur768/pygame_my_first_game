import pygame
from pygame.locals import *


class Entity:

    def __init__(self, health: int):

        self._rect = pygame.Rect(0, 0, 50, 50)
        self._health = health
