from .. import prepare
import pygame as pg

class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.speed = 0
        self.x = 0
        self.y = 0
        self.score = 0
        self.jumpHeight = 0
        self.state = 0
        self.direction = None

    def move(self, event):

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.x += 10

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
