"""
This module initializes the display.
Also contained are various constants used throughout the program.
"""
import os
import pygame
import csv
from . import tools
from data.components import player

pygame.init()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (153,0,153)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,128,0)
PINK = (255,51,153)
GRAY = (96,96,96)
TEAL = (51,255,255)
MAROON = (153,0,0)
LIME = (128,255,0)
NAVYBLUE = (0,0,153)
VIOLET = (204,153,255)
SKYBLUE = (28,92,140)

#screen size for game (1280, 1024)
SCREEN_SIZE = (1280, 900)

#cell size
CELL_SIZE = (48, 48)
PLAYER_SIZE = (48, 70)

#creates screen with screen size.
_screen = pygame.display.set_mode(SCREEN_SIZE)

#music
mainTheme = os.path.join('resources','music','Platformer_Main_Menu_Song.mp3')

#taken from game.py originally
clock = pygame.time.Clock()
debugMode = True #Leave TRUE for development
inputMode = "keyboard" #Change to joystick for PRODUCTION
chosenMode = "none"
loaded = False


#name of game
ORIGINAL_CAPTION = "SFA Platformer 0.1a"

#key color is purple
COLOR_KEY = (102, 0, 255)

#background color is shade of black
BACKGROUND_COLOR = (30, 40, 50)

#stores rectangle coordinate of screensize from top left corner.
SCREEN_RECT = pygame.Rect((0,0), SCREEN_SIZE)

#path of sfa logo for splash screen.
_ICON_PATH = os.path.join("resources", "tiles", "sfa_cube.png")

#sets window icon for game window
pygame.display.set_icon(pygame.image.load(_ICON_PATH))

#stores rectangle coordinate of screensize from top left corner.
SCREEN_RECT = pygame.Rect((0,0), SCREEN_SIZE)

_FONT_PATH = os.path.join("resources","fonts","Fixedsys500c.ttf")
SMALL_FONT = pygame.font.Font(_FONT_PATH, 25)

#background color is shade of black
BACKGROUND_COLOR = PURPLE

#creates screen with screen size.
_screen = pygame.display.set_mode(SCREEN_SIZE)

#creates game rectangle for speed


#Preloading screen
_screen.fill(BACKGROUND_COLOR)
_render = SMALL_FONT.render("CS students are slacking, please wait warmly~~", 0, pygame.Color("white"))
_screen.blit(_render, _render.get_rect(center=SCREEN_RECT.center))
pygame.display.update()
pygame.time.wait(500)

#The default controls for the game. CHANGE FOR JOYSTICK?
DEFAULT_CONTROLS = {pygame.K_DOWN  : "down",
                    pygame.K_UP    : "up",
                    pygame.K_LEFT  : "left",
                    pygame.K_RIGHT : "right"}

_TILE_DICTIONARY = { '1' : 'dirt_block.png',
                     '2' : 'gold_stone.png',
                     '3' : 'grass_block.png',
                     '4' : 'sfa_cube.png',
                     '5' : 'stone_block.png',
                     '6' : 'brick_block.png',}

GFX = tools.get_graphics(_TILE_DICTIONARY)


backGroundOne = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','skybox_one.jpg')).convert(), SCREEN_SIZE)
SPLASH1 = pygame.image.load(os.path.join('resources','image','SFA_CS_SPLASH.png'))
titlewords = pygame.image.load(os.path.join('resources','image','Titlename.png'))
playerImage = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','LumberjackMale.png')).convert_alpha(), PLAYER_SIZE)
playerImage2 = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','LumberjackMale.png')).convert_alpha(), PLAYER_SIZE)