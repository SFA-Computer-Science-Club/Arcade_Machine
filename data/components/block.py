#Class for a block, contains update functions/draw functions

import pygame
from .. import prepare, tools, logging

class Block():
    def __init__(self, x, y, name, image, rect, id):
        self.x = x
        self.y = y
        self.name = name
        self.image = image
        self.rect = rect
        self.id = id

    def draw(self):
        prepare._screen.blit(self.image, (self.x,self.y))

    