from .. import prepare, tools
import pygame as pg
from  ..components import world, collision
import math

SPEED = 1
JUMP_POWER = 5

class Player(tools._SpriteTemplate):
    """A class for the player"""
    def __init__(self, *groups):
        tools._SpriteTemplate.__init__(self, (0,0), prepare.PLAYER_SIZE, *groups)
        self.controls = prepare.DEFAULT_CONTROLS
        self.image = prepare.playerImage
        self.collider = collision.Collision()

        self.reset()

    def reset(self):
        """
        reset all variables for a fresh player.
        """
        pos = (100, 50)
        self.reset_position(pos)
        self.verticalVelocity = 0
        self.horizontalVelocity = 0
        self.direction = None
        self.score = 0
        self.state = 0
        self.health = 100
        self.collided = False
        self.canJump = True
        self.grounded = False
        self.collided = False
        self.collidedObjects = []

    def jump(self):
        if self.verticalVelocity < 0:
            self.verticalVelocity = 0
        self.verticalVelocity -= JUMP_POWER

    def applyGravity(self):
        self.verticalVelocity += 0.15

    def applyFriction(self):
        if (self.horizontalVelocity < -0.1):
            #left
            self.horizontalVelocity += 0.05
        elif (self.horizontalVelocity > 0.1):
            self.horizontalVelocity -= 0.05
        else:
            self.horizontalVelocity = 0


    def update(self):
        #Goal is to increment our vertical, and horizontal velocity
        #Then move that one by one, then resolve that in our collision
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            if self.horizontalVelocity > 3:
                self.horizontalVelocity = 3
            else:
                self.horizontalVelocity += 0.15 * SPEED
            if self.direction == "Left":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Right"
        if keys[pg.K_a]:
            if self.horizontalVelocity < -3:
                self.horizontalVelocity = -3
            else:
                self.horizontalVelocity -= 0.15 * SPEED
            if self.direction == "Right":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Left"
        if keys[pg.K_SPACE]:
            self.jump()
        if keys[pg.K_r]:
            self.reset()
        self.applyFriction()
        self.applyGravity()

        #after this point we have calculated all of our movement vectors, delta y and delta x

        newRect = self.rect
        newRect.y += self.verticalVelocity
        ccollided = self.collider.getCollidingObjects(newRect, world.WorldMap.mapOneObjTable)
        if (ccollided == False):
            #we can assume it isnt colliding on x axis, and that anything colliding will be on the y axis
            self.rect.y += self.verticalVelocity
            self.collided = False
        else:
            if (len(ccollided) == 1):
                #only one collided object
                collidedObject = ccollided[0]
                centerPlayer = newRect.centery
                centerObject = collidedObject.rect.centery
                self.collided = True

                if (centerPlayer - centerObject >= 0):
                    #player is below
                    self.rect.top = collidedObject.rect.bottom
                    self.verticalVelocity = 0
                    self.rect.y = self.rect.y
                else:
                    #player is ontop
                    self.rect.bottom = collidedObject.rect.top
                    self.verticalVelocity = 0
                    self.rect.y = self.rect.y

        newRect = self.rect
        newRect.x += self.horizontalVelocity 
        ccollided = self.collider.getCollidingObjects(newRect, world.WorldMap.mapOneObjTable)
        if ccollided == False:
            #nothing happened
            #self.rect.move(self.rect.x+self.horizontalVelocity,self.rect.y)
            self.rect.x += self.horizontalVelocity
            if (self.collided != True):
                self.collided = False
        else:
            self.collided = True
            #it did collide on x axis do things
            centerPlayer = newRect.centerx
            if (len(ccollided) == 1):
                collidedObject = ccollided[0]
                centerObject = collidedObject.rect.centerx
                if ((centerPlayer - centerObject) >= 0):
                    #player is to the right of the collided object
                    self.rect.left = collidedObject.rect.right
                    self.horizontalVelocity = 0
                    self.rect.x = self.rect.x
                else:
                    #player is to the left of the collided object
                    self.rect.right = collidedObject.rect.left
                    self.horizontalVelocity = 0
                    self.rect.x = self.rect.x
            else:
                pass
        
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y

    def draw(self, surface):
        if self.collided:
            pg.draw.rect(surface, prepare.GREEN, self.rect, 2)
        else:
            pg.draw.rect(surface, prepare.RED, self.rect, 2)
        #pg.draw.rect(surface, prepare.GREEN, (576,576,64,64),2)
        surface.blit(self.image, (self.rect.x, self.rect.y))