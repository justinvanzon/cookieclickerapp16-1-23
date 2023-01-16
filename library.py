import pygame
import pygame.image
from main import App
import sys
import os
import math
from pygame import font
from pygame.locals import *
import time
from threading import Timer

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
radius = 178
myfont_cookie = pygame.font.Font("CrimsonText-SemiBold.ttf", 45)
myfont_cookie1 = pygame.font.Font("CrimsonText-SemiBold.ttf", 35)
myfont_PC = pygame.font.Font("CrimsonText-SemiBold.ttf", 30)
myfont_PC1 = pygame.font.Font("CrimsonText-SemiBold.ttf", 32)
buildinginfoText = pygame.font.Font("CrimsonText-SemiBold.ttf", 20)
Cookies = 0
Price1 = 50
Price2 = 100
Price3 = 200
MouseClick = 0
Cookies_PC = 1
Cookies_CPS_HMMMMM = 0
DubbleBought = 0
pygame.time.set_timer(pygame.USEREVENT, 25)
pygame.time.set_timer(pygame.USEREVENT + 1, 50)
size = weight, height = 1920, 1080
flags = FULLSCREEN
screen = pygame.display.set_mode(size, flags)
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (size))
buildinginfo = pygame.image.load("buildinginfobackground.png").convert()
buildinginfo = pygame.transform.scale(buildinginfo, (350, 200))
imp = pygame.image.load("pixil-frame-0.png").convert_alpha()
rect = imp.get_rect(center=((weight / 2 - (weight / 2.8)), (height / 2) + (height / 30)))
stonk = pygame.image.load("STONKS.png").convert()
Penny = pygame.image.load("pennystocks.png").convert()
HMMMM = pygame.image.load("HMMMMMM.png").convert()
ClickAnimatie = [pygame.image.load('pixil-frame-0.png').convert_alpha(), pygame.image.load('pixil-frame-1.png').convert_alpha(), pygame.image.load('pixil-frame-2.png').convert_alpha(),
pygame.image.load('pixil-frame-3.png').convert_alpha(), pygame.image.load('pixil-frame-4.png').convert_alpha(),
pygame.image.load('pixil-frame-5.png').convert_alpha(), pygame.image.load('pixil-frame-6.png').convert_alpha()]
AnimatieCount = 0


