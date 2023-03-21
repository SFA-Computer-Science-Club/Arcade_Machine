from ... import prepare
from ..block import Block 
from .. import player
import time
from .. import world
import pygame

class Explosive(Block):
    def __init__(self, x, y, name, image, rect, id, damage):
        Block.__init__(self, x, y, name, image, rect, id)
        self.damage = damage
        self.exploded = False
        self.explodedTime = None

    def draw(self):
        if self.exploded != True:
            prepare._screen.blit(self.image, (self.x,self.y))
        else:
            if (time.time() - self.explodedTime < 1):
                prepare._screen.blit(prepare.explosiveSmokeTexture, (self.x,self.y))
            else:
                world.WorldMap.mapOneObjTable.remove(self)


    def onCollide(self, objectCollided):
        if (isinstance(objectCollided, player.Player)):
            #check if it is a player
            objectCollided.damagePlayer(self.damage)
            objectCollided.music.load(prepare.explosionSound)
            objectCollided.music.play(0)
            self.exploded = True
            self.explodedTime = time.time()
            self.x -= 64
            self.y -= 64
