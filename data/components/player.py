from .. import prepare
import pygame as pg
from  ..components import world, collision
import math

class Player(object):
    def __init__(self):
        self.image = prepare.playerImage
        self.health = 100
        self.collider = collision.Collision()
        self.speed = 1
        self.music = pg.mixer.music
        self.verticalVelocity = 0
        self.horizontalVelocity = 0
        self.x = 100
        self.y = 50
        self.finished = False
        self.finishMessage = ""
        self.rect = prepare.playerImage.get_rect().move(self.x,self.y)
        self.score = 0
        self.jumpPower = 5
        self.state = 0
        self.currJump = 0
        self.direction = None
        self.collided = False
        self.canJump = True
        self.grounded = False
        self.collided = False
        self.closestBlock = None

    def jump(self):
        if self.canJump == False:
            return
        if self.verticalVelocity < 0:
            self.verticalVelocity = 0
        if self.currJump == 1:
            self.verticalVelocity -= self.jumpPower * 1.5
        else:   
            self.verticalVelocity -= self.jumpPower
        self.currJump += 1
        if self.currJump == 2:
            self.canJump = False

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
        #this fires event events
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.jump()

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
        if keys[pg.K_r]:
            self.y = 50
            self.x = 100
            self.verticalVelocity = 0
            self.horizontalVelocity = 0
        self.applyFriction()
        self.applyGravity()

        #after this point we have calculated all of our movement vectors, delta y and delta x
        #maybe rounding the numbers help?
        #add the velocity to the x and y, then just make sure you round them when you pass it to the function

        newVelocityY = round(self.y + self.verticalVelocity)

        newRect = self.rect
        newRect.y = newVelocityY
        ccollided = self.collider.getCollidingObjects(newRect, world.WorldMap.mapOneObjTable)
        if (ccollided == False):
            #we can assume it isnt colliding on x axis, and that anything colliding will be on the y axis
            self.y += self.verticalVelocity
            self.rect.y = newVelocityY
            self.collided = False
        else:
            self.collided = True
            if (len(ccollided) == 1):
                #only one collided object
                collidedObject = ccollided[0]

                collidedObject.onCollide(self)
                if collidedObject.canCollide == False:
                    self.y += self.verticalVelocity
                    self.rect.y = newVelocityY
                    self.collided = False
                else:
                    centerPlayer = newRect.centery
                    centerObject = collidedObject.rect.centery

                    if (centerPlayer - centerObject > 0):
                        #player is below
                        self.rect.top = collidedObject.rect.bottom
                        self.verticalVelocity = 0
                        self.y = self.rect.y
                    else:
                        #player is ontop
                        self.rect.bottom = collidedObject.rect.top
                        self.verticalVelocity = 0
                        self.y = self.rect.y
                        self.canJump = True
                        self.currJump = 0
            else:
                closestBlock = None
                closestNum = 0
                for tile in ccollided:
                    tile.onCollide(self)
                    if (tile.canCollide == False):
                        continue
                    if closestBlock == None:
                        #first loop
                        closestBlock = tile
                        closestNum = abs(tile.rect.centery - newRect.centery)
                    if abs(tile.rect.centery - newRect.centery) < closestNum:
                        #something is closer
                        closestBlock = tile
                self.closestBlock = closestBlock
                #now we have our closest tile
                if (self.rect.centery - closestBlock.rect.centery > 0):
                    #means that the closest block is above is
                    self.rect.top = closestBlock.rect.bottom
                    self.y = self.rect.y
                    self.verticalVelocity = 0
                else:
                    #we are ontop of something
                    self.canJump = True
                    self.currJump = 0
                    self.rect.bottom = closestBlock.rect.top
                    self.verticalVelocity = 0
                    self.y = self.rect.y

        newRect = self.rect
        newVelocityX = round(self.x + self.horizontalVelocity)
        newRect.x = newVelocityX
        
        ccollided = self.collider.getCollidingObjects(newRect, world.WorldMap.mapOneObjTable)
        if ccollided == False:
            #nothing happened
            #self.rect.move(self.x+self.horizontalVelocity,self.y)
            self.x += self.horizontalVelocity
            if (self.collided != True):
                self.collided = False
        else:
            self.collided = True
            #it did collide on x axis do things
            centerPlayer = newRect.centerx
            if (len(ccollided) == 1):
                collidedObject = ccollided[0]

                #doTheObject's onCollide
                collidedObject.onCollide(self)
                if collidedObject.canCollide == False:
                    self.x += self.horizontalVelocity
                    if (self.collided != True):
                        self.collided = False
                else:
                    centerObject = collidedObject.rect.centerx
                    if ((centerPlayer - centerObject) >= 0):
                        #player is to the right of the collided object
                        self.rect.left = collidedObject.rect.right
                        self.horizontalVelocity = 0
                        self.x = self.rect.x
                    else:
                        #player is to the left of the collided object
                        self.rect.right = collidedObject.rect.left
                        self.horizontalVelocity = 0
                        self.x = self.rect.x
            else:
                closestBlock = None
                closestNum = 0
                for tile in ccollided:
                    tile.onCollide(self)
                    if (tile.canCollide == False):
                        continue
                    if closestBlock == None:
                        #first loop
                        closestBlock = tile
                        closestNum = abs(tile.rect.centerx - newRect.centerx)
                    if abs(tile.rect.centerx - newRect.centerx) < closestNum:
                        #something is closer
                        closestBlock = tile
                self.closestBlock = closestBlock
                #now we have our closest tile
                if (self.rect.centerx - closestBlock.rect.centerx > 0):
                    self.rect.left = closestBlock.rect.right
                    self.x = self.rect.x
                    self.horizontalVelocity = 0
                else:
                    self.rect.right = closestBlock.rect.left
                    self.horizontalVelocity = 0
                    self.x = self.rect.x
        
        self.rect.x = newRect.x
        self.rect.y = newRect.y

    def damagePlayer(self, value: int):
        #do some damage to the player
        self.health -= abs(value)
        if self.health <= 0:
            self.finished = False
            self.health = 100
            self.y = 50
            self.x = 100
            self.verticalVelocity = 0
            self.horizontalVelocity = 0
            

    def draw(self, surface):
        font = pg.font.Font(prepare._FONT_PATH, 24)
        img = font.render("Health: " + str(self.health), True, prepare.RED)
        if (self.finished):
            img2 = font.render(self.finishMessage, True, prepare.LIME)
            surface.blit(img2, (self.x,self.y-60))
        surface.blit(self.image, (self.x, self.y))
        surface.blit(img, (self.x,self.y))
        