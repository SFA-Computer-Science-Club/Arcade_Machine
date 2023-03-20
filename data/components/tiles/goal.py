from ... import prepare
from ..block import Block 
from .. import player
import pygame

class Goal(Block):
    def __init__(self, x, y, name, image, rect, id, message):
        Block.__init__(self, x, y, name, image, rect, id)
        self.message = message

    def onCollide(self, objectCollided):
        if (isinstance(objectCollided, player.Player)):
            #check if it is a player
            if (objectCollided.finished != True):
                objectCollided.finished = True
                objectCollided.finishMessage = self.message
                objectCollided.music.load(prepare.victorySound)
                objectCollided.music.play(0)