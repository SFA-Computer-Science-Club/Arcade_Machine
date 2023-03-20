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

    def startup(self, now, persistant):
        """
        Call the parent class' startup method
        """
        state_machine._State.startup(self, now, persistant)
        if self.reset_map:
            #reset game to beginning and reset all variables.
            self.player = player.Player()
            self.world = world.WorldMap(self.player)
            self.reset_map = False
    
    def get_event(self, event):
        self.player.move(event)
        pass

    def update(self, keys, now):
        """Update phase for the primary game state."""
        self.now = now
        self.world.update(now)

    def draw(self, surface, interpolate):
        """Draw level and HUD(soontm)"""
        self.world.draw(surface, interpolate)       