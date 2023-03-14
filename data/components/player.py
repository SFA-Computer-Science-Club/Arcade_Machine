from .. import prepare
import pygame as pg

class Player(object):
    def __init__(self, x, y):
        self.image = prepare.playerImage
        self.rect = self.image.get_rect()
        self.health = 100
        self.speed = 4
        self.verticalVelocity = 0
        self.rect.x = x
        self.rect.y = y
        self.score = 0
        self.jumpPower = 5
        self.state = 0
        self.direction = None
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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
        for row in prepare.level_one_tiles:
            for tile in row:
                if tile[1].colliderect(self.rect.x, self.rect.y + self.verticalVelocity, self.width, self.height):
                    self.y += 0
                    
        self.applyGravity()
        self.y += self.verticalVelocity

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
