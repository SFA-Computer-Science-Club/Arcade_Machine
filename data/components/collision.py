import pygame

class Collision:
    def __init__(self):
        pass

    def getCollidingObjects(self, objectToTest, objectTable):
        collidingObjects = []
        for object in objectTable:
            # Check if player's current coordinates are inside of each rect in mapOneRectTable\
            if objectToTest.rect.colliderect(object.rect):      
                collidingObjects.append(object)
        if len(collidingObjects) > 0:
            #not empty, we did collide with something
            return collidingObjects
        else:
            return False