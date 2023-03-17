from .. import prepare
import pygame as pg
from  ..components import world, collision

class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.collider = collision.Collision()
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
        if (self.horizontalVelocity < -0.1):
            #left
            self.horizontalVelocity += 0.05
        elif (self.horizontalVelocity > 0.1):
            self.horizontalVelocity -= 0.05
        else:
            self.horizontalVelocity = 0

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

                #after we resolved x collision, apply y collision

        newRect = self.rect
        newRect.y += self.verticalVelocity
        newRect.x = self.x
        collided = self.collider.getCollidingObjects(newRect, world.WorldMap.mapOneObjTable)

        if (collided == False):
            #we can assume it isnt colliding on x axis, and that anything colliding will be on the y axis
            self.y += self.verticalVelocity
        elif (self.verticalVelocity != 0):
            if (len(collided) == 1):
                #only one collided object
                collidedObject = collided[0]
                centerPlayer = newRect.centery
                centerObject = collidedObject.rect.centery

                if (centerPlayer - centerObject > 0):
                    #player is below
                    overLapY = newRect.top - collidedObject.rect.bottom
                    self.y += self.verticalVelocity - overLapY
                else:
                    #player is ontop
                    overLapY = newRect.bottom - collidedObject.rect.top
                    self.y += self.verticalVelocity - overLapY 
            self.verticalVelocity = 0

        newRect = self.rect
        newRect.x += self.horizontalVelocity   
        newRect.y = self.y 
        collided = self.collider.getCollidingObjects(newRect, world.WorldMap.mapOneObjTable)

        if collided == False:
            #nothing happened
            #self.rect.move(self.x+self.horizontalVelocity,self.y)
            self.x += self.horizontalVelocity
            self.collided = False
        elif (self.horizontalVelocity != 0):
            self.collided = True
            #it did collide on x axis do things
            centerPlayer = newRect.centerx
            if (len(collided) == 1):
                collidedObject = collided[0]
                centerObject = collidedObject.rect.centerx
                if ((centerPlayer - centerObject) > 0):
                    #player is to the right of the collided object
                    overLapX = newRect.left - collidedObject.rect.right
                    #self.rect.move(self.x + self.horizontalVelocity + overLapX, self.y)
                    self.x += self.horizontalVelocity - overLapX
                else:
                    #player is to the left of the collided object
                    overLapX = newRect.right - collidedObject.rect.left
                    #self.rect.move(self.x + self.horizontalVelocity - overLapX, self.y)
                    self.x += self.horizontalVelocity - overLapX
            else:
                pass
            self.horizontalVelocity = 0
        
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        if self.collided:
            pg.draw.rect(surface, prepare.GREEN, self.rect, 2)
        else:
            pg.draw.rect(surface, prepare.RED, self.rect, 2)
        #pg.draw.rect(surface, prepare.GREEN, (576,576,64,64),2)
        surface.blit(self.image, (self.x, self.y))