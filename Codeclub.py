import pygame, random,sys,time
from pygame.locals import *

FPS= 30
WINDOWWIDTH= 640
WINDOWHEIGHT = 480
FLASHSPEED = 500
FLASHDELAY = 200
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4

WHITE = (255,255,255)
BLACK = (0,0,0)
BRIGHTRED =(255,0,0)
RED = (155,0,0)
BRIGHTGREEN = (0,255,0)
GREEN = (0,155,0)
BRIGHTBLUE =(0,0,255)
BLUE = (0,0,155)
BRIGHTYELLOW = (255,255,0)
YELLOW = (155,155,0)
DARKGRAY = (40,40,40)

bgColor = BLACK

XMARGIN =int((WINDOWWIDTH-(2*BUTTONSIZE)-BUTTONGAPSIZE)/2)
YMARGIN =int((WINDOWHEIGHT-(2*BUTTONSIZE)-BUTTONGAPSIZE)/2)

YELLOWRECT = pygame.Rect(XMARGIN,YMARGIN,BUTTONSIZE,BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE,YMARGIN,BUTTONSIZE,BUTTONSIZE)
RECRECT = pygame.Rect(XMARGIN,YMARGIN+BUTTONSIZE+BUTTONGAPSIZE,BUTTONSIZE,BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE,YMARGIN+BUTTONSIZE+BUTTONGAPSIZE,BUTTONSIZE,BUTTONSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF ,BASICFONT , BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("CODECLUB")

    BASICFONT = pygame.font.Font("freesansbold.ttf", 16)

    infoSurf = BASICFONT.render("Please Match the Pattern by Clicking Button or Using the Q,W,A,S keys",1,DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT-25)
    BEEP1 = pygame.mixer.Sound("beep1.ogg")
    BEEP2 = pygame.mixer.Sound("beep2.ogg")
    BEEP3 = pygame.mixer.Sound("beep3.ogg")
    BEEP4 = pygame.mixer.Sound("beep4.ogg")
    
    pattern = []
    currentStep = 0
    lastClickTime = 0
    score = 0

    waitingForInput = False

    while True:
        clickedButton = None
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        ScoreSurf = BASICFONT.render("Score: " + str(score),1,WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH-100,10)
        DISPLAYSURF.blit(scoreSurf,scoreRect)
        DISPLAYSURF.blit(infoSurf,infoRect)
        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex , mousey = event.pos
                clickedButton = getButtonClicked(nousex,mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == k_w:
                    clickedButton = BLUE
                elif event.key == k_a:
                    clickedButton = RED
                elif event.key = k_s:
                    clickedButton = GREEN
        if not waitingForInput:
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice(YELLOW,BLUE,RED,GREEN))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True



