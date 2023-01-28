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
                        prepare._screen.blit(prepare.dirtTexture, (x,y))    
                        # prepare._screen.draw(prepare.dirtTexture, (x,y))               
                    elif column == '2':
                        prepare._screen.blit(prepare.goldStoneTexture, (x,y))
                    elif column == '3':
                        prepare._screen.blit(prepare.grassTexture, (x,y))
                    elif column == '4':
                        prepare._screen.blit(prepare.sfaCubeTexture, (x,y))           
                    elif column == '5':
                        prepare._screen.blit(prepare.stoneTexture, (x,y))
                    elif column == '6':
                        prepare._screen.blit(prepare.brickBlockTexture, (x,y))
    
    def update(self, now):
        self.load(self.name)

    def draw(self, surface, interpolate):
        self.load(self.name)
