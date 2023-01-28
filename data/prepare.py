"""
This module initializes the display.
Also contained are various constants used throughout the program.
"""
import os
import pygame

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

#music
mainTheme = os.path.join('resources','music','Platformer_Main_Menu_Song.mp3')

#taken from game.py originally
clock = pygame.time.Clock()
debugMode = True #Leave TRUE for development
inputMode = "keyboard" #Change to joystick for PRODUCTION
chosenMode = "none"
loaded = False

#screen size for game
SCREEN_SIZE = (1280, 1000)

#name of game
ORIGINAL_CAPTION = "SFA Platformer 0.1a"

#key color is purple
COLOR_KEY = (102, 0, 255)

#background color is shade of black
BACKGROUND_COLOR = (30, 40, 50)

#stores rectangle coordinate of screensize from top left corner.
SCREEN_RECT = pygame.Rect((0,0), SCREEN_SIZE)

#path of sfa logo for splash screen.
_ICON_PATH = os.path.join("resources", "image", "sfa_cube.png")

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

#fill screen with background_color
_screen.fill(BACKGROUND_COLOR)

#The default controls for the game. CHANGE FOR JOYSTICK?
DEFAULT_CONTROLS = {pygame.K_DOWN  : "down",
                    pygame.K_LEFT  : "left",
                    pygame.K_RIGHT : "right"}

#Tile dimensions
TILE_DIMENSION = (64,64)
x = 64
y = 64

#maps
testMap = os.path.join('resources','map_data','TestMap.csv')
testMap2 = os.path.join('resources','map_data','TestMap2.csv')
testMap3 = os.path.join('resources','map_data','TestMap3.csv')
testMap4 = os.path.join('resources','map_data','TestMap4.csv')


#You can define some sprites or images here
dirtTexture = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','dirt_block.png')).convert(), TILE_DIMENSION)
grassTexture = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','grass_block.png')).convert(), TILE_DIMENSION)
stoneTexture = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','stone_block.png')).convert(), TILE_DIMENSION)
backGroundOne = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','skybox_one.jpg')).convert(), (1280,1280))
goldStoneTexture = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','gold_stone.png')).convert(), TILE_DIMENSION)
brickBlockTexture = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','brick_block.png')).convert(), TILE_DIMENSION)
sfaCubeTexture = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','sfa_cube.png')).convert(), TILE_DIMENSION)
SPLASH1 = pygame.image.load(os.path.join('resources','image','SFA_CS_SPLASH.png'))
titlewords = pygame.image.load(os.path.join('resources','image','Titlename.png'))
playerImage = pygame.transform.scale(pygame.image.load(os.path.join('resources','image','LumberjackMale.png')), TILE_DIMENSION)


#preload screen
_render = SMALL_FONT.render("CS students are slacking, please wait warmly~~", 0, pygame.Color("white"))
_screen.blit(_render, _render.get_rect(center=SCREEN_RECT.center))
pygame.display.update()
pygame.time.wait(1000)