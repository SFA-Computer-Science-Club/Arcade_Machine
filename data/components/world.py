import os
import sys
import pygame as pg
from csv import reader
from .. import prepare, tools, logging

class WorldMap(object):
    def __init__(self):
        self.name = prepare.testMap2
        self.loaded = prepare.loaded
        self.scrolling = False

    def load(self, world_name):
        """Load world given a world_name."""
        if self.loaded == False:
            self.loaded = True
            #do some initial things
            logging.writeLog(f" {world_name}: loading for first time")
<<<<<<< Updated upstream
        prepare._screen.blit(pg.transform.scale(prepare.backGroundOne, prepare.SCREEN_SIZE), (0,0))  
       
        # open file in read mode
        with open(world_name, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for rowIndex, row in enumerate(csv_reader):
                for columnIndex, column in enumerate(row):
                    x = columnIndex * 64
                    y = rowIndex * 64
                    if column == '1':
                        prepare._screen.blit(pg.transform.scale(prepare.dirtTexture, (64,64)), (x,y))                    
                    elif column == '2':
                        prepare._screen.blit(pg.transform.scale(prepare.goldStoneTexture, (64,64)), (x,y))
                    elif column == '3':
                        prepare._screen.blit(pg.transform.scale(prepare.grassTexture, (64,64)), (x,y))
                    elif column == '4':
                        prepare._screen.blit(pg.transform.scale(prepare.sfaCubeTexture, (64,64)), (x,y))                    
                    elif column == '5':
                        prepare._screen.blit(pg.transform.scale(prepare.stoneTexture, (64,64)), (x,y))
                    elif column == '6':
                        prepare._screen.blit(pg.transform.scale(prepare.brickBlockTexture, (64,64)), (x,y))
=======
        prepare._screen.blit(prepare.backGroundOne, (0,0))         

        # pass the file object to reader() to get the reader object
        # Iterate over each row in the csv using reader object
        for rowIndex, row in enumerate(prepare.mapOneTable):
            for columnIndex, column in enumerate(row):
                x = columnIndex * 64
                y = rowIndex * 64
                if prepare.mapOneTable[rowIndex][columnIndex] == -1:
                    continue
                else:
                    # this means that it isn't an air block so just put what value it is in the array
                    prepare._screen.blit(prepare.mapOneTable[rowIndex][columnIndex], (x,y))
>>>>>>> Stashed changes
    
    def update(self, now):
        self.load(self.name)

    def draw(self, surface, interpolate):
        self.load(self.name)
<<<<<<< Updated upstream
=======

    def collision(self, player):
        didCollide = False
        for rowIndex, row in enumerate(prepare.mapOneRectTable):
            
            # Check if player's current coordinates are inside of each rect in mapOneRectTable\
            rectObject = prepare.mapOneRectTable[rowIndex]
            if player.rect.colliderect(rectObject):
                
                player.collide(rectObject)
                
                didCollide = True
        if (didCollide == False):
            player.collided = False
>>>>>>> Stashed changes
