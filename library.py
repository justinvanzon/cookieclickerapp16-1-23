import pygame
import sys
import os
import math
from pygame import font
from pygame.locals import *
pygame.init()
pygame.font.init()
radius = 448  # EVEN KIJKEN HOEVEEL
myfont_cookie = pygame.font.SysFont("arial", 50)
myfont_PC = pygame.font.SysFont("arial", 25)
myfont_click = pygame.font.SysFont("arial", 22)
Cookies = 0
Price1 = 50
Price2 = 100
PcUpgradesPrice = 50
Cookies_PC = 1
Cookies_CPS = 0
pygame.time.set_timer(pygame.USEREVENT, 25)
size = weight, height = 1920, 1080
screen = pygame.display.set_mode(size)
MouseClick = 0
positions = []
pygame.time.set_timer(pygame.USEREVENT + 1, 400)
pygame.time.set_timer(pygame.USEREVENT + 3, 50)