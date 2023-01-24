"""
The main game loop is here
"""

# Started 10/5/2022
# Simple mario-style platform game
# Add whatever you want I just put some comments
# Note on assets, use 16x16 for blocks (grass, brick, whatever), characters can be anything*

#Init some needed libraries
#Make sure pygame 2+ is installed! Very important
from csv import reader
import pygame
from . import classes
import os
import subprocess
import random
from . import prepare
from . import logging


if os.name == "posix":
    #Linux
    output = subprocess.Popen("xrandr  | grep '\*' | cut -d' ' -f4", shell=True, stdout=subprocess.PIPE).communicate()[0] # Returns (WxH)
    stringSize = str(output, 'utf-8').split('x')
    SCREEN_WIDTH = int(stringSize[0])
    SCREEN_HEIGHT = int(stringSize[1])
else:
    print(os.name)

def game():
    """
    The main game loop.
    """
    global loaded
    global chosenMode
    mapLevel = None
    pygame.init()
    mainscreen = pygame.display.set_mode(prepare.SCREEN_SIZE)
    #pygame.display.toggle_fullscreen()
    pygame.display.set_caption(prepare.ORIGINAL_CAPTION)
    player = classes.Player()
    player.setHealth(20)
    logging.createLog()
    logging.writeLog("Application starting")

    background = pygame.Surface(mainscreen.get_size())
    background = background.convert()
    background.fill(prepare.WHITE)

    #Platformer Game Level 1
    def levelOne():
        global loaded
        global mapLevel
        if prepare.loaded == False:
            loaded = True
            #do some initial things
            logging.writeLog("Level one loading for first time")
            #mapLevel = 
        
        #mainscreen.fill(levelOneMap.skyColor)
        mainscreen.blit(pygame.transform.scale(prepare.backGroundOne, prepare.SCREEN_SIZE), (0,0))  
       
        # open file in read mode
        with open(prepare.testMap2, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for rowIndex, row in enumerate(csv_reader):
                for columnIndex, column in enumerate(row):
                    x = columnIndex * 64
                    y = rowIndex * 64
                    if column == '1':
                        mainscreen.blit(pygame.transform.scale(prepare.dirtTexture, (64,64)), (x,y))                    
                    elif column == '2':
                        mainscreen.blit(pygame.transform.scale(prepare.goldStoneTexture, (64,64)), (x,y))
                    elif column == '3':
                        mainscreen.blit(pygame.transform.scale(prepare.grassTexture, (64,64)), (x,y))
                    elif column == '4':
                        mainscreen.blit(pygame.transform.scale(prepare.sfaCubeTexture, (64,64)), (x,y))                    
                    elif column == '5':
                        mainscreen.blit(pygame.transform.scale(prepare.stoneTexture, (64,64)), (x,y))
                    elif column == '6':
                        mainscreen.blit(pygame.transform.scale(prepare.brickBlockTexture, (64,64)), (x,y))

    if prepare.inputMode == "keyboard":
        logging.writeLog("Starting keyboard mode")
    elif prepare.inputMode == "joystick":
        logging.writeLog("Starting joystick mode")
    else:
        logging.writeLog("No input type selected, shutting down")
        return 1



    while True: #Main game loop
        for event in pygame.event.get(): #Loops through every event, can be keyboard or mouse input etc
            if event.type == pygame.QUIT:
                logging.writeLog("Process ending, nominal shutdown")
                return 0
        if prepare.chosenMode == "none":
            #ask user to choose mode or pull up main screen or something
            prepare.chosenMode = "levelOne"
            logging.writeLog("Level One mode chosen")
        if prepare.chosenMode == "levelOne":
            levelOne()
        prepare.clock.tick(60)
        pygame.display.flip()

