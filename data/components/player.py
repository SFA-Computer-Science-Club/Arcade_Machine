from .. import prepare
import pygame as pg


class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.speed = 4
        self.x = 100
        self.y = 200
        self.score = 0
        self.jumpHeight = 0
        self.state = 0
        self.direction = None

    def move(self, event):
        if prepare.joysticks[0].get_axis(0) > .9:
            self.x += 10
        elif prepare.joysticks[0].get_axis(0) == -1:
            self.x -= 10
        
    def update(self):
        pass
        # if self.direction == "right":
        #     self.x += 1
    

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
