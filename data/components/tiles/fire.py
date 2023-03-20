from ... import prepare
from ..block import Block 
from .. import player
import pygame

class Fire(Block):
    def __init__(self, x, y, name, image, rect, id, damage):
        Block.__init__(self, x, y, name, image, rect, id)
        self.damage = damage

    def onCollide(self, objectCollided):
        if (isinstance(objectCollided, player.Player)):
            #check if it is a player
            if (pygame.time.get_ticks() % 10 == 0):
                objectCollided.damagePlayer(self.damage)