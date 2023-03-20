import os
import sys
import pygame as pg
from csv import reader
from .. import prepare, tools, logging
from . import block, level

class WorldMap(object):
    def __init__(self, player):
        self.player = player
        self.world_name = "TestMap2.csv"
        self.loaded = prepare.loaded
        self.world_file = self.load(self.world_name)
        self.scrolling = False
        self.scroll_vector = None
        start_coords = None
        self.level = level.Level(self.player, self.world_file)

    def notused(self):
        #Create all of the objects
        id = 0
        with open(self.name, 'r') as read_obj:
            csv_reader = prepare.csv.reader(read_obj)
            for rowIndex, row in enumerate(csv_reader):
                for columnIndex, column in enumerate(row):
                        x = columnIndex * prepare.CELL_SIZE[0]
                        y = rowIndex * prepare.CELL_SIZE[1]
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
                            sfaBlock.rect.x = x
                            print("x: ", x," y:",y)
                            sfaBlock.rect.y = y
                            self.mapOneObjTable.append(sfaBlock)     
                        elif column == '5':
                            stoneBlock = block.Block(x,y,"stone_block",prepare.stoneTexture,prepare.stoneTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(stoneBlock)
                        elif column == '6':
                            brickBlock = block.Block(x,y,"brick_block",prepare.brickBlockTexture,prepare.brickBlockTexture.get_rect().move(x,y), id)
                            self.mapOneObjTable.append(brickBlock)
                        id += 1
    
    def load(self, name):
        """Load world given a world_name."""
        path = os.path.join(".","resources","map_data",name)
        if self.loaded == False:
            self.loaded = True
            # do some initial things
            logging.writeLog(f" {name}: loading for first time")
        return path
    
    def update(self, now):
        self.level.update(now)

    def draw(self, surface, interpolate):
        self.level.draw(surface, interpolate)
