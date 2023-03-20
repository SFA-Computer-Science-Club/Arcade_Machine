import os
import sys
import pygame as pg

from .. import prepare, tools



class Tile(tools._SpriteTemplate):
    """basic tile."""
    def __init__(self, source, target, id, mask):
        """If the player can collide with it pass mask=True."""
        tools._SpriteTemplate.__init__(self, target, prepare.CELL_SIZE)
        self.name = prepare._TILE_DICTIONARY[source]
        self.image = prepare.GFX[self.name]
        self.id = id
        if mask:
            self.mask = pg.mask.from_surface(self.image)

    @property
    def get_data(self):
        return (self.id, self.name, self.rect)

    def collide_with_player(self, player):
        """
        any sprite that will need to find collision with the player must
        have this method.
        """
        print(self.get_name, self.rect)
        player.collide_with_solid()
    
    def update(self, *args):
        self.rect.topleft = self.exact_position

class Level(object):
    """class to represent a single map level."""
    def __init__(self, player, map_name):
        self.player = player
        self.name = map_name
        self.background = self.make_background()
        self.main_sprites = pg.sprite.Group(self.player)
        
        self.solids = self.make_tile_group(True)
        self.all_group = pg.sprite.Group(self.solids, self.player)
        self.group_dict = {"main" : self.main_sprites,
                           "solids" : self.solids,
                           "all" : self.all_group,
                           }

    def make_background(self):
        return prepare.backGroundOne

    def make_tile_group(self, mask=False):
        """
        Creates a single sprite group.
        Pass mask=True to create collision masks for the tiles.
        could add layers and special tiles features here in the future.
        """
        group = pg.sprite.Group()
        x, y = prepare.CELL_SIZE
        id = 0
        with open(self.name, 'r') as read_obj:
            csv_reader = prepare.csv.reader(read_obj)
            for rowIndex, row in enumerate(csv_reader):
                for columnIndex, column in enumerate(row):
                    if column != '-1':
                        group.add(Tile(column, (columnIndex*x,rowIndex*y), id, mask))   
                    id += 1
        return group

    def update(self, now):
        """
        Update all sprites; check any collisions that may have occured;
        """
        groups = pg.sprite.Group(self.solids)
        self.all_group.update(now, self.player, groups, self.group_dict)
        # hits = self.check_collisions()
        # self.player.collision_is_done(self.player, hits)

    def NOTUSED_check_collisions(self):
        """
        Check collisions and call the appropriate functions of the affected sprites.
        """
        callback = tools.rect_then_mask
        groups = pg.sprite.Group(self.solids)
        hits = pg.sprite.spritecollide(self.player, groups, False, callback)
        for hit in hits:
            hit.collide_with_player(self.player)

    def draw(self, surface, interpolate):
        """Draw all sprites and background to the surface."""
        surface.blit(self.background, (0,0))
        self.all_group.draw(surface)
        self.player.draw_hitbox(surface)