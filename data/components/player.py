from .. import prepare
import pygame as pg

class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.speed = 4
        self.verticalVelocity = 0
        self.x = 100
        self.y = 200
        self.score = 0
        self.jumpPower = 5
        self.state = 0
        self.direction = None

    def jump(self):
        if self.verticalVelocity < 0:
            self.verticalVelocity = 0
        self.verticalVelocity -= self.jumpPower

    def applyGravity(self):
        self.verticalVelocity += 0.15

    def move(self, event):
        if event[pg.K_d]:
            self.x += 1 * self.speed
            if self.direction == "Left":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Right"
        if event[pg.K_a]:
            self.x -= 1 * self.speed
            if self.direction == "Right":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Left"
        if event[pg.K_SPACE]:
            self.jump()
        if event[pg.K_r]:
            self.y = 200
            self.x = 100
            self.verticalVelocity = 0

    def update(self):
        self.applyGravity()
        self.y += self.verticalVelocity

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
