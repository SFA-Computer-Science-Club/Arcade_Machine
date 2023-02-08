from .. import prepare
import pygame as pg

class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.speed = 4
        self.verticalVelocity = 0
        self.x = 900
        self.y = 200
        self.rect = prepare.playerImage.get_rect().move(self.x,self.y)
        self.score = 0
        self.jumpPower = 5
        self.state = 0
        self.direction = None
        self.collided = False
        self.canJump = True
        self.canLeft = True
        self.canRight = True

    def jump(self):
        if self.verticalVelocity < 0:
            self.verticalVelocity = 0
        self.verticalVelocity -= self.jumpPower

    def applyGravity(self):
        if self.collided == True:
            self.verticalVelocity = 0
            return
        self.verticalVelocity += 0.15

    def move(self, event):
        if event[pg.K_d]:
            if not self.canRight:
                return
            self.x += 1 * self.speed
            if self.direction == "Left":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Right"
        if event[pg.K_a]:
            if not self.canLeft:
                return
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
        self.rect.x = self.x
        self.rect.y = self.y
        self.applyGravity()
        self.y += self.verticalVelocity

    def collide(self, collidedPart):
        self.collided = True
        #Check which axis it collided on, top left right or bottom
        if (collidedPart.left - self.rect.right) < 0: #Means the part is to the left of the player
            self.canLeft = False
        elif (collidedPart.right - self.rect.left) > 0: #Part is to the right of player
            self.canRight = False

    def draw(self, surface):
        if self.collided:
            if not self.canLeft:
                pg.draw.rect(surface, prepare.BLUE, self.rect, 2)
            elif not self.canRight:
                pg.draw.rect(surface, prepare.GREEN, self.rect, 2)
            else:
                pg.draw.rect(surface, prepare.RED, self.rect, 2)
        surface.blit(self.image, (self.x, self.y))