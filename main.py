import time

from opslag import *

positions = []



class MouseObject:
    def __init__(self, image, location, speed, height):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(location)
        self.height = height

    def move(self):
        self.pos = self.pos.move(0, self.speed)

    def check(self):
        if self.pos[1] <= self.height[1] - 82:
            return positions.pop(0)

class HMMMMM:
    def on_loop(self):
        if 1720 <= mouse_pos[0] <= 1770 and 10 <= mouse_pos[1] <= 60:
            screen.blit(buildinginfo, (1370, 10))  #
            HMMMMInfo = buildinginfoText.render(('Verdubbelt de CPS van Penny Stocks'), True, (255, 255, 255))
            HMMMMInfo1 = buildinginfoText.render('kost: ' + str('{:1,.0f}'.format(Price3, ',')), True, (255, 255, 255))
            screen.blit(HMMMMInfo, (1400, 30))
            screen.blit(HMMMMInfo1, (1400, 48))

    def on_event(self, event):
        global Price3, Cookies, Cookies_CPS_HMMMMM, DubbleBought
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1720 <= mouse_pos[0] <= 1770 and 10 <= mouse_pos[1] <= 60 and Price3 <= Cookies:
                Cookies -= Price3                                               # KNOP
                Price3 = (Price3 * 3)
                Cookies_CPS_HMMMMM *= 2
                DubbleBought += 1

class STONKS:
    def on_loop(self):
        if 1720 <= mouse_pos[0] <= 1920 and 65 <= mouse_pos[1] <= 145:
            screen.blit(buildinginfo, (1370, 65))
    #        HMMMMInfo = buildinginfoText.render(('Verdubbelt de CPS van Penny Stocks'), True, (255, 255, 255))
     #       HMMMMInfo1 = buildinginfoText.render('kost: ' + str('{:1,.0f}'.format(Price3, ',')), True, (255, 255, 255))
      #      screen.blit(HMMMMInfo, (1400, 30))
       #     screen.blit(HMMMMInfo1, (1400, 48))

    def on_event(self,event):
        global Cookies, Cookies_PC, MouseClick, mouse_pos, Price1
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            dist_x = mouse_pos[0] - rect.centerx + 3
            dist_y = mouse_pos[1] - rect.centery
            if radius > math.hypot(dist_x, dist_y):
                Cookies += Cookies_PC                                       #CLICK OP KOEKJE EVENT
                MouseClick += 1
                rendermouse = myfont_PC1.render(str('{:1,.0f}'.format(Cookies_PC, ',')), True, (240, 240, 240))
                o = MouseObject(rendermouse, mouse_pos, -2, mouse_pos)
                positions.append(o)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1720 <= mouse_pos[0] <= 1920 and 65 <= mouse_pos[1] <= 145 and Price1 <= Cookies:
                Cookies -= Price1                                               #STONKS KNOP
                Price1 = (Price1 * 2.1)
                Cookies_PC *= 2
                screen.blit(pc_text1, (1728, 108))

class PENNY:
    def on_loop(self):
        global CPSUP
        if 1720 <= mouse_pos[0] <= 1920 and 145 <= mouse_pos[1] <= 225:
            if DubbleBought == 0:
                CPSUP = 1
            if DubbleBought > 0:
                CPSUP = (2 ** DubbleBought)
            screen.blit(buildinginfo, (1370, 145))
            PENNYInfo = buildinginfoText.render(('door te investeren in Penny stocks'), True, (255, 255, 255))
            PENNYInfo1 = buildinginfoText.render('krijg je ' + str('{:1,.0f}'.format(CPSUP, ',') +  ' koekje per seconde'), True, (255, 255, 255))
            PENNYInfo2 = buildinginfoText.render('kost: ' + str('{:1,.0f}'.format(Price2, ',')), True, (255, 255, 255))
            PENNYInfo3 = buildinginfoText.render('verdient ' + str('{:1,.0f}'.format(Cookies_CPS_HMMMMM, ',') + ' koekjes per seconde'), True, (255, 255, 255))
            screen.blit(PENNYInfo, (1400, 165))
            screen.blit(PENNYInfo1, (1400, 184))
            screen.blit(PENNYInfo2, (1400, 220))
            screen.blit(PENNYInfo3, (1400, 255))

    def on_event(self, event):
        global Price2, Cookies_CPS_HMMMMM, Cookies, DubbleBought, mouse_pos, CPSUP
        #       if event.type == pygame.MOUSEMOTION:
        #          mouse_pos1 = pygame.mouse.get_pos()
        #         if 1720 <= mouse_pos1[0] <= 1770 and 10 <= mouse_pos1[1] <= 60:
        #            screen.blit(buildinginfo, (130, 10))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1720 <= mouse_pos[0] <= 1920 and 145 <= mouse_pos[1] <= 225 and Price2 <= Cookies:
                Cookies -= Price2  # PENNT STOCKS KNOP
                Price2 *= 1.165
                Cookies_CPS_HMMMMM += CPSUP
                screen.blit(pc_text2, (1728, 188))


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = size


    def on_init(self):
        pygame.init()
        self._display_surf = screen
        self._running = True
        self.openFile()

    def openFile(self):
        global Cookies, Cookies_PC, Price1, Price2, Cookies_CPS_HMMMMM, MouseClick, Price3, DubbleBought, CPSUP
        f = open('scratch.txt', 'r')
        file = f.readlines()
        if Cookies == False:
            self.closeFile()
        Cookies = int(file[0])
        Price1 = int(file[1])
        Cookies_PC = int(file[2])
        Price2 = int(file[3])
        Cookies_CPS_HMMMMM = int(file[4])
        MouseClick = int(file[5])
        Price3 = int(file[6])
        DubbleBought = int(file[7])
        if DubbleBought == 0:
            CPSUP = 1
        if DubbleBought > 0:
            CPSUP = (2 ** DubbleBought)
        f.close()

    def closeFile(self):
        global Cookies, Price1, Cookies_PC, Price2, Cookies_CPS_HMMMMM, MouseClick, price3, DubbleBought
        f = open('scratch.txt', 'w')
        f.write(str(int(Cookies)) + "\n")
        f.write(str(int(Price1)) + "\n")
        f.write(str(int(Cookies_PC)) + "\n")
        f.write(str(int(Price2)) + "\n")
        f.write(str(int(Cookies_CPS_HMMMMM)) + "\n")
        f.write(str(int(MouseClick)) + "\n")
        f.write(str(int(Price3)) + "\n")
        f.write(str(int(DubbleBought)))
        f.close()

    def on_loop(self):
        global positions, o, score_text, AnimatieCount, mouse_pos, Cookies_CPS_HMMMMM, Cookies_CPS
        mouse_pos = pygame.mouse.get_pos()
        Cookies_CPS = Cookies_CPS_HMMMMM
        HMMMMM.on_loop(self)
        STONKS.on_loop(self)
        PENNY.on_loop(self)
        for o in positions:
            o.check()
        score_text = myfont_cookie1.render('per seconde: ' + str('{:1,.0f}'.format(Cookies_CPS, ',')), True, (255, 255, 255))
        cookiesamount = myfont_cookie.render('Cookies: ' + str('{:1,.0f}'.format(Cookies, ',')), True, (255, 255, 255))
        #if len(positions) == 0:
        #    AnimatieCount = 0
        #if AnimatieCount > 5:
         #   AnimatieCount = 0
        #screen.blit(ClickAnimatie[AnimatieCount//5], rect)
        #NOG IETS RENDERED KOEKJE
        screen.blit(score_text, (10, 30))
        screen.blit(cookiesamount, (10, -10))
        for o in positions:
            o.check()
            o.move()
            screen.blit(o.image, (o.pos[0], o.pos[1] - 35))  # INSTELLEN DAT MOUSE_POS[0] SCALED MET GETAL
        pygame.display.update()
        clock.tick(60)

    def on_event(self, event):
        global radius, rect, Cookies, Cookies_PC, mouse_pos, Price1, Cookies_CPS, positions, MouseClick, o, \
            rendermouse, pc_text, pc_text1, AnimatieCount, pc_text2, Price3, DubbleBought, mouse_pos1, Cookies_CPS_HMMMMM
        if event.type == pygame.QUIT:
            self._running = False
        pc_text1 = myfont_PC.render(str('{:1,.0f}'.format(Price1, ',')), True, (0, 0, 0))
        pc_text2 = myfont_PC.render(str('{:1,.0f}'.format(Price2, ',')), True, (0, 0, 0))
        if event.type == pygame.USEREVENT:
            Cookies_CPS = Cookies_CPS_HMMMMM
            Cookies += (Cookies_CPS / 40)
        #if event.type == pygame.USEREVENT + 1:
        #    AnimatieCount += 1
        STONKS.on_event(self, event)
        PENNY.on_event(self, event)
        HMMMMM.on_event(self, event)

    def on_render(self):
        global radius, rect, myfont, Cookies, imp, background
        pygame.display.set_caption('Cooooookies')
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(imp, rect)
        screen.blit(stonk, (1720, 65))
        screen.blit(pc_text1, (1728, 108))
        screen.blit(Penny, (1720, 145))
        screen.blit(pc_text2, (1728, 188))
        screen.blit(HMMMM, (1720, 10))


    def on_cleanup(self):
        self.closeFile()
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