import os
import sys
import pygame as pg
from csv import reader
from .. import prepare, tools, logging
from . import block
from .tiles.fire import Fire
from .tiles.goal import Goal
from .tiles.explosive import Explosive


class WorldMap(object):
    mapOneObjTable = []
    def __init__(self):
        self.name = prepare.testMap2
        self.loaded = prepare.loaded
        self.scrolling = False

        #Create all of the objects
        id = 0
        with open(self.name, 'r') as read_obj:
            csv_reader = prepare.csv.reader(read_obj)
            for rowIndex, row in enumerate(csv_reader):
                for columnIndex, column in enumerate(row):
                        x = columnIndex * 64
                        y = rowIndex * 64
                        if column == '1':
                            dirtBlock = block.Block(x,y,"dirt_block",prepare.dirtTexture,prepare.dirtTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(dirtBlock)
                        elif column == '2':
                            goldStoneBlock = block.Block(x,y,"gold_stone_block",prepare.goldStoneTexture,prepare.goldStoneTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(goldStoneBlock)
                        elif column == '3':
                            grassBlock = block.Block(x,y,"grass_block",prepare.grassTexture,prepare.grassTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(grassBlock)
                        elif column == '4':
                            sfaBlock = block.Block(x,y,"sfa_block",prepare.sfaCubeTexture,prepare.sfaCubeTexture.get_rect().move(x,y), id)
                            sfaBlock.setCollidable(False)
                            self.mapOneObjTable.append(sfaBlock)     
                        elif column == '5':
                            stoneBlock = block.Block(x,y,"stone_block",prepare.stoneTexture,prepare.stoneTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(stoneBlock)
                        elif column == '6':
                            brickBlock = block.Block(x,y,"brick_block",prepare.brickBlockTexture,prepare.brickBlockTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(brickBlock)
                        elif column == '7':
                            fireBlock = Fire(x,y,"fire_block",prepare.fireTexture, prepare.fireTexture.get_rect().move(x,y), id, 1)
                            fireBlock.setCollidable(False)
                            self.mapOneObjTable.append(fireBlock)
                        elif column == '8':
                            flagBlock = Goal(x,y, "goal_block", prepare.goalTexture, prepare.goalTexture.get_rect().move(x,y), id, "You won!")
                            flagBlock.setCollidable(False)
                            self.mapOneObjTable.append(flagBlock)
                        elif column == '9':
                            explosiveBlock = Explosive(x,y, "explosive_block", prepare.explosiveTexture, prepare.explosiveTexture.get_rect().move(x,y), id, 100)
                            explosiveBlock.setCollidable(False)
                            self.mapOneObjTable.append(explosiveBlock)
                        id += 1

    
    def load(self, world_name):
        """Load world given a world_name."""
        if self.loaded == False:
            self.loaded = True
            # do some initial things
            logging.writeLog(f" {world_name}: loading for first time")
        prepare._screen.blit(prepare.backGroundOne, (0,0))         

        # pass the file object to reader() to get the reader object
        # Iterate over each row in the csv using reader object
        for object in self.mapOneObjTable:
            object.draw()
    
    def update(self, now, player):
        self.load(self.name)

    def draw(self, surface, interpolate):
        self.load(self.name)