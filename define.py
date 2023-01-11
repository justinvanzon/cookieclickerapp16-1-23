import pygame
import sys
import os
import math
from pygame import font
from pygame.locals import *
pygame.init()
pygame.font.init()

class File(self):
    def openFile(self):
        global Cookies, PcUpgradesBought, Cookies_PC, Price1, Price2, Cookies_CPS, MouseClick
        f = open('scratch.txt', 'r')
        file = f.readlines()
        Cookies = int(file[0])
        Price1 = int(file[1])
        Cookies_PC = int(file[2])
        Price2 = int(file[3])
        Cookies_CPS = int(file[4])
        MouseClick = int(file[5])
        f.close()


    def closeFile(self):
        global Cookies, Price1, Cookies_PC, Price2, Cookies_CPS, MouseClick
        f = open('scratch.txt', 'w')
        f.write(str(int(Cookies)) + "\n")
        f.write(str(int(Price1)) + "\n")
        f.write(str(int(Cookies_PC)) + "\n")
        f.write(str(int(Price2)) + "\n")
        f.write(str(int(Cookies_CPS)) + "\n")
        f.write(str(int(MouseClick)))
        f.close()

