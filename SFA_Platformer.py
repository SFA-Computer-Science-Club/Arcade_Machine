"""
SFA platformer game starter.
"""

import sys
import pygame as pg
from data.main import main
import cProfile
import pstats

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()