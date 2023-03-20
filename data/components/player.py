from .. import prepare, tools
import pygame as pg
from  ..components import world, collision
import math

SPEED = 1.0
JUMP_POWER = 2

class Player(tools._SpriteTemplate):
    """A class for the player"""
    def __init__(self, *groups):
        tools._SpriteTemplate.__init__(self, (0,0), prepare.PLAYER_SIZE, *groups)
        self.controls = prepare.DEFAULT_CONTROLS
        self.name = "Lumberjack"
        self.image = prepare.playerImage
        self.direction = None
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
        self.score = 0
        self.state = 0
        self.currJump = 0
        self.direction = None
        self.health = 100
        self.collided = False
        self.canJump = True
        self.grounded = False
        self.collided = False
        self.collidedObjects = []

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
        math.ceil(self.verticalVelocity)

    def applyFriction(self):
        if (self.horizontalVelocity < -0.1):
            #left
            self.horizontalVelocity += 0.05
        elif (self.horizontalVelocity > 0.1):
            self.horizontalVelocity -= 0.05
        else:
            self.horizontalVelocity = 0
        math.ceil(self.horizontalVelocity)

    def move(self, event):
        #this fires event events
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.jump()

    def update(self, now, player, solids, *args):
        #Goal is to increment our vertical, and horizontal velocity
        #Then move that one by one, then resolve that in our collision
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            if self.horizontalVelocity > 3:
                self.horizontalVelocity = 3
            else:
                self.horizontalVelocity += 0.15 * SPEED
            if self.direction == "Right":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Left"
        if keys[pg.K_a]:
            if self.horizontalVelocity < -3:
                self.horizontalVelocity = -3
            else:
                self.horizontalVelocity -= 0.15 * SPEED
            if self.direction == "Left":
                self.image = pg.transform.flip(self.image, True, False)
            self.direction = "Left"
        if keys[pg.K_r]:
            self.reset()
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
                collidedObject = ccollided
                centerPlayer = newRect.centery
                centerObject = collidedObject.rect.centery

                if (centerPlayer - centerObject > 0):
                    #player is below
                    self.rect.top = collidedObject.rect.bottom
                    self.verticalVelocity = 0
                    self.rect.y = self.rect.y
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
                    print("bottom")
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
            #self.rect.move(self.rect.x+self.horizontalVelocity,self.rect.y)
            self.rect.x += self.horizontalVelocity
            if (self.collided != True):
                self.collided = False
        else:
            self.collided = True
            #it did collide on x axis do things
            centerPlayer = newRect.centerx
            if (ccollided != False):
                collidedObject = ccollided
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
                closestBlock = None
                closestNum = 0
                for tile in ccollided:
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


    def check_collisions(self, player, groups):
        """
        Check collisions and call the appropriate functions of the affected sprites.
        """
        callback = tools.rect_then_mask
        hits = pg.sprite.spritecollide(player, groups, False, callback)
        print(hits)
        if not hits:
            return False
        else:
            for hit in hits:
                if hit.get_name != 'Lumberjack':
                    # print(hit.get_data)
                    return hit
                else: return False
                    # hit.collide_with_player(self.rect)
                    # pg.draw.rect(surface, prepare.RED, self.rect, 2)

    def draw_hitbox(self, surface):
        if self.collided:
            pg.draw.rect(surface, prepare.GREEN, self.rect, 2)
        else:
            pg.draw.rect(surface, prepare.RED, self.rect, 2)
        #pg.draw.rect(surface, prepare.GREEN, (576,576,64,64),2)
        # surface.blit(self.image, self.rect)
    
    def collide_with_solid(self):
        # print("player collided with solid")
        self.exact_position = self.old_position[:]
        self.rect.topleft = self.exact_position
