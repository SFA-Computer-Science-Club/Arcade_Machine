import pygame
import prepare

tile = prepare.dirtTexture
print(tile.get_rect())
tile = tile.get_rect().move(128, 128)
print(tile.get_rect())

