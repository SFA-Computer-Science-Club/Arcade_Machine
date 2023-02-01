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
            # do some initial things
            logging.writeLog(f" {world_name}: loading for first time")
        prepare._screen.blit(prepare.backGroundOne, (0,0))         
        # prepare._screen.blit(pg.transform.scale(prepare.backGroundOne, prepare.SCREEN_SIZE), (0,0))  

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
    
    def update(self, now, player):
        self.load(self.name)
        self.collision(player)

    def draw(self, surface, interpolate):
        self.load(self.name)

    def collision(self, player):
        for rowIndex, row in enumerate(prepare.mapOneRectTable):
            for columnIndex, column in enumerate(row):
                x = columnIndex * 64
                y = rowIndex * 64
                
                # Check if player's current coordinates are inside of each rect in mapOneRectTable\
                # if prepare.mapOneRectTable[rowIndex][columnIndex]:
