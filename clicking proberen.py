from library import *
mouse_pos = pygame.mouse.get_pos()

class App:
    def __init__(self):
        self.openFile()
        self._running = True
        self._display_surf = None
        self.size = size

    def on_init(self):
        pygame.init()
        self._display_surf = screen
        self._running = True

    def click_display(self):
        global positions
        if len(positions) == 0:
            pygame.time.set_timer(pygame.USEREVENT + 4, 300, 1)
        if len(positions) == 1:
            pygame.time.set_timer(pygame.USEREVENT + 5, 300, 1)
        if len(positions) == 2:
            pygame.time.set_timer(pygame.USEREVENT + 6, 300, 1)
        if len(positions) == 4:
            pygame.time.set_timer(pygame.USEREVENT + 7, 300, 1)
        if len(positions) == 5:
            pygame.time.set_timer(pygame.USEREVENT + 8, 300, 1)
        if len(positions) == 6:
            pygame.time.set_timer(pygame.USEREVENT + 9, 300, 1)
        if len(positions) == 7:
            pygame.time.set_timer(pygame.USEREVENT + 10, 300, 1)
        if len(positions) == 8:
            pygame.time.set_timer(pygame.USEREVENT + 11, 300, 1)
        if len(positions) == 9:
            pygame.time.set_timer(pygame.USEREVENT + 12, 300, 1)
        if len(positions) == 10:
            pygame.time.set_timer(pygame.USEREVENT + 13, 300, 1)

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

    def on_loop(self):
        global Price1, myfont_PC, PcUpgradesPrice, click_text, mouse_pos, positions
        score_text = myfont_cookie.render('Cookies: ' + str(int(Cookies)), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        score_text = myfont_cookie.render('per seconde: ' + str(int(Cookies_CPS)), True, (255, 255, 255))
        screen.blit(score_text, (320, 10))
        pc_text = myfont_PC.render(str(int(Price1)), True, (255, 255, 255))
        screen.blit(pc_text, (220, 90))
        pc_text = myfont_PC.render(str(int(Price2)), True, (255, 255, 255))
        screen.blit(pc_text, (220, 140))
        click_text = myfont_click.render(str(int(Cookies_PC)), True, (255, 255, 255))
        for mouse_pos in positions:
            screen.blit(click_text, (mouse_pos[0] - 10, mouse_pos[1] - 35))
        pygame.display.flip()

    def on_event(self, event):
        global radius, rect, Cookies, Cookies_PC, mouse_pos, Price1, Cookies_CPS, click_text, positions, MouseClick, X, Z, YY, new_positions
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.USEREVENT:
            Cookies += (Cookies_CPS / 40)
        if event.type == pygame.USEREVENT + 4 and len(positions) > 0:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 5 and len(positions) > 1:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 6 and len(positions) > 2:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 7 and len(positions) > 3:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 8 and len(positions) > 4:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 9 and len(positions) > 5:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 10 and len(positions) > 6:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 11 and len(positions) > 7:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 12 and len(positions) > 8:
            positions.remove(mouse_pos)
        if event.type == pygame.USEREVENT + 13 and len(positions) > 9:
            positions.remove(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dist_x = mouse_pos[0] - rect.centerx - 7
            dist_y = mouse_pos[1] - rect.centery + 35
            if radius > math.hypot(dist_x, dist_y):
                Cookies += Cookies_PC
                MouseClick += 1
                positions.insert(0, mouse_pos)
                self.click_display()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse_pos[0] <= 210 and 80 <= mouse_pos[1] <= 130 and Price1 <= Cookies:
                Cookies -= Price1
                Price1 = (Price1 * 2.1)
                Cookies_PC *= 2

    def aandacht(self, event):
        global Price2, Cookies_CPS, Cookies
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse_pos[0] <= 210 and 130 <= mouse_pos[1] <= 180 and Price2 <= Cookies:
                Cookies -= Price2
                Price2 *= 1.165
                Cookies_CPS += 1


    def on_render(self):
        global radius, rect, myfont, Cookies
        pygame.display.set_caption('Cooooookies')
        screen.fill((0, 0, 0))
        imp = pygame.image.load("biscuit-cookie-monster-clipart-24.png")
        imp = pygame.transform.scale(imp, (1000, 1000))
        rect = imp.get_rect(center=(weight / 2, height / 2))
        stonk = pygame.image.load("STONKS.png")
        screen.blit(stonk, (10, 80))
        aandacht = pygame.image.load("AANDACHT.png")
        screen.blit(aandacht, (10, 130))
        screen.blit(imp, rect)

    def on_cleanup(self):
        self.closeFile()
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
                self.aandacht(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()