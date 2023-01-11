import pygame
import sys
import os
import math

from pygame import font
from pygame.locals import *
pygame.init()
pygame.font.init()

radius = 448  # EVEN KIJKEN HOEVEEL
myfont = pygame.font.SysFont("arial", 50)
Cookies = 0
Cookies_PC = 1
size = weight, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = size

    def openFile():
        global f
        f = open('scratch.txt', 'r')
        file = f.readlines()
        last = int(file[0])

    def closeFile():
        f.close()
        file = open('scratch.txt')


    def on_init(self):
        pygame.init()
        self._display_surf = screen
        self._running = True

    def on_loop(self):
        score_text = myfont.render('Cookies: ' + str(Cookies), True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        pygame.display.update()

    def on_event(self, event):
        global radius, rect, Cookies, Cookies_PC
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            dist_x = mouse_pos[0] - rect.centerx - 7
            dist_y = mouse_pos[1] - rect.centery + 35
            if radius > math.hypot(dist_x, dist_y):
                Cookies += Cookies_PC

    def on_render(self):
        global radius, rect, myfont, Cookies
        pygame.display.set_caption('Cooooookies')
        screen.fill((0, 0, 0))
        imp = pygame.image.load("biscuit-cookie-monster-clipart-24.png")
        imp = pygame.transform.scale(imp, (1000, 1000))
        rect = imp.get_rect(center=(weight / 2, height / 2))
        screen.blit(imp, rect)


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()




if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()