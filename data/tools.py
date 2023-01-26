"""
This module contains the basic Control class.
Can hold future resource helper functions.
"""

import os
import pygame as pg
from . import state_machine

TIME_PER_UPDATE = 16.0 #Milliseconds

class Control(object):
    """
    Control class for entire game. Contains the game loop, and the event_loop to pass events to States.
    """
    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.caption = caption
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.fps_visible = True
        self.now = 0.0
        self.keys = pg.key.get_pressed()
        self.state_machine = state_machine.StateMachine()

    def update(self):
        """
        Updates the currently active state.
        """
        self.now = pg.time.get_ticks()
        self.state_machine.update(self.keys, self.now)

    def draw(self, interpolate):
        if not self.state_machine.state.done:
            self.state_machine.draw(self.screen, interpolate)
            pg.display.update()
            self.show_fps()
    
    def event_loop(self):
        """
        Process all events and pass them down to the state_machine.
        The f5 key globally turns on/off the display of FPS in the caption
        """
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                pass
                # self.toggle_show_fps(event.key)

            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            self.state_machine.get_event(event)
        self.state_machine.get_key_event(keys)

    
    # def toggle_show_fps(self,key):


    def show_fps(self):
        """
        Display the current FPS
        """
        fps = self.clock.get_fps()
        with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
        pg.display.set_caption(with_fps)

    def main(self):
        """
        Main loop for entire program. Uses a constant timestep.
        """
        #To ensure that the movement is based on time rather than frame rate, 
        #Clock is used to tell you how long (in fractions of a second) it has been since the last update. 
        #If you multiply that time delta value by all of your speeds, those speeds become "movement per second" instead of "movement per frame". 
        #This also helps hide dramatic shifts in frame rates while the game is running (due to loading and whatnot).
        lag = 0.0
        while not self.done:
            lag += self.clock.tick(self.fps)
            self.event_loop()
            while lag >= TIME_PER_UPDATE:
                self.update()
                lag -= TIME_PER_UPDATE
            self.draw(lag/TIME_PER_UPDATE)

class Timer(object):
    """
    A simple timer for non-animation Events.
    """
    def __init__(self, delay, ticks=-1):
        """
        The delay is given in milliseconds; ticks is the number of ticks the
        timer will make before flipping self.done to True.  Pass a value
        of -1 to bypass this.
        """
        self.delay = delay
        self.ticks = ticks
        self.tick_count = 0
        self.timer = None
        self.done = False

    def check_tick(self, now):
        """Returns true if a tick worth of time has passed."""
        if not self.timer:
            self.timer = now
            return True
        elif not self.done and now-self.timer > self.delay:
            self.tick_count += 1
            self.timer = now
            if self.ticks != -1 and self.tick_count >= self.ticks:
                self.done = True
            return True
# add tools for animations, sprites, loading/parsing resources, collision.