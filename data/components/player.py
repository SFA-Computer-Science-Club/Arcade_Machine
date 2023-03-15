from .. import prepare
import pygame as pg

class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.speed = 1
        self.verticalVelocity = 0
        self.horizontalVelocity = 0
        self.x = 100
        self.y = 50
        self.rect = prepare.playerImage.get_rect().move(self.x,self.y)
        self.score = 0
        self.jumpPower = 5
        self.state = 0
        self.direction = None
        self.collided = False
        self.canJump = True
        self.grounded = False
        self.collided = False
        self.collidedObjects = []

    def jump(self):
        if self.verticalVelocity < 0:
            self.verticalVelocity = 0
        self.verticalVelocity -= self.jumpPower

    def applyGravity(self):
        self.verticalVelocity += 0.15

    def applyFriction(self):
        if (self.horizontalVelocity < 0):
            #left
            self.horizontalVelocity += 0.05
        elif (self.horizontalVelocity > 0):
            self.horizontalVelocity -= 0.05

    def move(self, event):
        pass

    def update(self):
        #Goal is to increment our vertical, and horizontal velocity
        #Then move that one by one, then resolve that in our collision
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            if self.horizontalVelocity > 3:
                self.horizontalVelocity = 3
            else:
                self.horizontalVelocity += 0.15 * self.speed
            if self.direction == "Left":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Right"
        if keys[pg.K_a]:
            if self.horizontalVelocity < -3:
                self.horizontalVelocity = -3
            else:
                self.horizontalVelocity -= 0.15 * self.speed
            if self.direction == "Right":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Left"
        if keys[pg.K_SPACE]:
            self.jump()
        if keys[pg.K_r]:
            self.y = 50
            self.x = 100
            self.verticalVelocity = 0
            self.horizontalVelocity = 0
        self.applyFriction()
        self.applyGravity()

        #after this point we have calculated all of our movement vectors, delta y and delta x
        self.x += self.horizontalVelocity
        
        

        #after we resolved x collision, apply y collision
        self.y += self.verticalVelocity

    def draw(self, surface):
        if self.collided:
            pg.draw.rect(surface, prepare.RED, self.rect, 2)
        surface.blit(self.image, (self.x, self.y))