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
        prepare._screen.blit(prepare.backGroundOne, (0,0))         
        #prepare._screen.blit(pg.transform.scale(prepare.backGroundOne, prepare.SCREEN_SIZE), (0,0))  

        # pass the file object to reader() to get the reader object
        # Iterate over each row in the csv using reader object
        for row in prepare.level_one_tiles:
            for tile in row:
                # TEMP FIX: no tile should be empty, however, some are 
                # getting past my filter in prepare.py. Need to fix and
                # remove this if statement.
                if len(tile) == 0:
                    continue
                prepare._screen.blit(tile[0], tile[1])         
    
    def update(self, now):
        self.load(self.name)

    def draw(self, surface, interpolate):
        self.load(self.name)
