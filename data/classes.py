""" Contains classes for characters and enemies"""

class Entity:

    """Entity class, can be things like characters or enemies"""
    # def __init__(self):
    #     #log entity created
    #     print("spawned")

    def setHealth(self, helth):
        self.health = helth

    def setIcon(self, iconpath):
        self.icon = iconpath

    def doDamage(self, damage):
        self.health = self.health - damage
        #You can probably add the damage sound here
        if self.health <= 0:
            #Dead
            return 0

    def setSpeed(self, spd):
        self.speed = spd

    def setImage(self, imagepath):
        self.image = imagepath

class Player(Entity):
    
    score = None
    level = None

class Pickup(Entity):
    print("Pickup") #Things like hearts or some sort of equivalent