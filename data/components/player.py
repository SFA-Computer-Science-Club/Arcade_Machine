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
        if event[pg.K_d]:
            self.x += 1 * self.speed
        if event[pg.K_a]:
            self.x -= 1 * self.speed
        if event[pg.K_s]:
            self.y += 1 * self.speed
        if event[pg.K_w]:
            self.y -= 1 * self.speed

        # if event.type == pg.KEYUP:
        #     self.direction = None
        # elif event.type == pg.KEYDOWN:
        #     self.direction = "right"
        # if event.type == pg.K_RIGHT:
        #     self.x += 1
        #     self.draw()
        # elif event.type == pg.K_LEFT:
        #     self.x -= 1
        
    def update(self):
        pass
        # if self.direction == "right":
        #     self.x += 1
    

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
