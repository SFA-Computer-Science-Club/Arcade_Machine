from .. import prepare
import pygame as pg

class Player(object):
    def __init__(self):
        self.image = pg.transform.scale(prepare.playerImage, prepare.TILE_DIMENSION)
        self.controls = prepare.DEFAULT_CONTROLS
        self.health = 100
        self.speed = 0
        self.x = 0
        self.y = 0
        self.score = 0
        self.jumpHeight = 0
        self.state = 0
        self.direction = "right"
        self.direction_stack = []

    def add_direction(self, key):
        if key in self.controls:
            direction = self.controls[key]
            if direction in self.direction_stack:
                self.direction_stack.remove(direction)
            self.direction_stack.append(direction)            

    def pop_direction(self, key):
        if key in self.controls:
            direction = self.controls[key]
            if direction in self.direction_stack:
                self.direction_stack.remove(direction)

    
    
    def jump(self):
        pass

    def move(self):
        if self.direction_stack:
            self.direction = self.direction_stack[-1]
            if self.direction == "right":
                self.x += 3
            elif self.direction == "left":
                self.x += -3

        # if event.type == pg.KEYUP:
        #     self.direction = None
        # elif event.type == pg.KEYDOWN:
        #     self.direction = "right"
        # if event.type == pg.K_RIGHT:
        #     self.x += 1
        #     self.draw()
        # elif event.type == pg.K_LEFT:
        #     self.x -= 1
        
    def update(self, now):
        self.move()
    

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
