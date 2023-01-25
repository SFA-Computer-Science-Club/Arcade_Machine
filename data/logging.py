"""
Contains classes for logging.
toggle On/Off here.
"""

import datetime
import os
import pygame as pg
from . import prepare

#Set True for logging and False for no logging.
doLogging = True

#If doLogging is True, setup log file.
if doLogging:
    currentWorkDirectory = os.getcwd()
    pathToLogFolder = currentWorkDirectory + "/data/" + "/log/"
    logFile = pathToLogFolder + str(datetime.date.today()) + "-" + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second) + ".txt"

def createLog():
    if doLogging == False:
        return
    logfile = open(logFile, "w")
    logfile.write("Log Created\nPygame Version: {}\nPlatformer version: {}\nInputMode: {}\nDebugMode: {}\nCurrentDirectory: {}".format(pg.version.ver, prepare.ORIGINAL_CAPTION, prepare.inputMode, prepare.debugMode, currentWorkDirectory)) #Writes some basic things upon creation
    logfile.close()

def writeLog(input):
    if doLogging == False:
        return
    logfile = open(logFile, "a")
    logfile.write("\n" + input) #Writes a new line given an input
    logfile.close()