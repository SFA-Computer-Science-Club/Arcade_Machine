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
        self.player = player.Player(100, 200)

    def startup(self, now, persistant):
        """
        Call the parent class' startup method
        """
        state_machine._State.startup(self, now, persistant)
        if self.reset_map:
            #reset game to beginning and reset all variables.
            self.world = world.WorldMap()
    
    def get_event(self, event):
        pass
        # if event.type == pg.KEYDOWN:
        #     self.player.move(event)

    def get_key_event(self, keyEvent):
        self.player.move(keyEvent)


    def update(self, keys, now):
        self.now = now
        self.world.update(now)
        self.player.update()

    def draw(self, surface, interpolate):
        self.world.draw(surface, interpolate)
        self.player.draw(surface)


        