import pygame as pg
# from .. import classes
import os
import subprocess
import random
from .. import prepare, state_machine, logging
from  ..components import world, player

class Game(state_machine._State):
    """Core state for the gameplay."""
    def __init__(self):
        state_machine._State.__init__(self)
        self.world = None
        self.reset_map = True
        self.player = player.Player()

    def startup(self, now, persistant):
        """
        Call the parent class' startup method
        """
        state_machine._State.startup(self, now, persistant)
        if self.reset_map:
            #reset game to beginning and reset all variables.
            self.world = world.WorldMap()
    
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.player.move(event)


    def update(self, keys, now):
        self.now = now
        self.world.update(now)
        self.player.update()

    def draw(self, surface, interpolate):
        self.world.draw(surface, interpolate)
        self.player.draw(surface)


        