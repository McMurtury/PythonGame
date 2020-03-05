import pygame, sys, Image_dir
from pygame.locals import *
from Image_dir import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Testing')

mouse_x = 0
mouse_y = 0


corner1 = (300, 400)
corner2 = (400, 400)




#questions text format
fontObj = pygame.font.Font('FFF_Tusj-webfont.ttf', 60)
textSurfaceObj = fontObj.render('Choose your race', True, Image_dir.SGRAY)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 100)
check = fontObj.render('Are you sure?', True, SGRAY)
checkrect = check.get_rect()
checkrect.center = (300, 100)
genderq = fontObj.render('Are you male or female?', True, SGRAY)
genderqRectObj = textSurfaceObj.get_rect()
genderqRectObj.center = (300, 100)
nameq = fontObj.render('What is your name?', True, SGRAY)
namerect = check.get_rect()
namerect.center = (300, 100)

#yes/no text format
yes = fontObj.render('Yes', True, GREEN)
yesrect = yes.get_rect()
yesrect.center = (200, 400)
no = fontObj.render('No', True, BLUE)
norect = no.get_rect()
norect.center = (600, 400)
selection = pygame.font.Font ('FFF_Tusj-webfont.ttf', 100)

#race text format
elf = fontObj.render ('Elf', True, GREEN)
elfrect = elf.get_rect()
elfrect.center = (200, 300)
elfs = selection.render ('Elf', True, GREEN)
elfsrect = elfs.get_rect()
elfsrect.center = (200, 300)
human = fontObj.render ('Human', True, BLUE)
humanrect = human.get_rect()
humanrect.center = (600, 300)
humans = selection.render ('Human', True, BLUE)
humansrect = humans.get_rect()
humansrect.center = (600, 300)

#gender text format
male = fontObj.render ('Male', True, NAVY)
malerect = male.get_rect()
malerect.center = (200, 300)
males = selection.render ('Male', True, NAVY)
malesrect = males.get_rect()
malesrect.center = (200, 300)
female = fontObj.render ('Female', True, PURPLE)
femalerect = female.get_rect()
femalerect.center = (600, 300)
females = selection.render ('Female', True, PURPLE)
femalesrect = females.get_rect()
femalesrect.center = (600, 300)

def name(N):
    
    x = 1
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    N[0] += evt.unicode
                elif evt.key == K_BACKSPACE:
                    N[0] = N[0][:-1]
                elif evt.key == K_RETURN:
                    N[0] = N[0]
                    x = 0                    
            elif evt.type == QUIT:
                 return
        
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(nameq, namerect)
        block = font.render(N[0], True, NAVY)
        rect = block.get_rect()
        rect.center = DISPLAYSURF.get_rect().center
        DISPLAYSURF.blit(block, rect)
        pygame.display.update()
        
        if x == 0:
            
            break
def disname():
    fontname = pygame.font.Font('FFF_Tusj-webfont.ttf', 60)
    textSurfaceObj = fontname.render(player_char[0], True, (0, 0, 128))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 75)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.flip()
	
def race (R):
    while True:
        x = 0
        y = 0
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit (elf, elfrect)
        DISPLAYSURF.blit (human, humanrect)
        pygame.display.update()
        if x == 0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        if mouse_x <= corner1[0]:
                            while y == 0:
                                DISPLAYSURF.fill(WHITE)
                                DISPLAYSURF.blit(check, checkrect)
                                DISPLAYSURF.blit(elfs, elfsrect)
                                DISPLAYSURF.blit(no, norect)
                                DISPLAYSURF.blit(yes, yesrect)
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_x <= corner1[0]:
                                                R[1] = 'Elf'
                                                x = 1
                                                return
                                            elif mouse_x >= corner2[0]:
                                                y = 1
                                                
                                            
                        
                        elif mouse_x >= corner2[0]:
                            while y == 0:
                                DISPLAYSURF.fill(WHITE)
                                DISPLAYSURF.blit(check, checkrect)
                                DISPLAYSURF.blit(humans, humansrect)
                                DISPLAYSURF.blit(no, norect)
                                DISPLAYSURF.blit(yes, yesrect)
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_x <= corner1[0]:
                                                R[1] = 'Human'
                                                x = 1
                                                return
                                            elif mouse_x >= corner2[0]:
                                                y = 1
        elif x == 1:
            break

def gender (G):
    while True:
        x = 0
        y = 0
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(genderq, genderqRectObj)
        DISPLAYSURF.blit (male, malerect)
        DISPLAYSURF.blit (female, femalerect)
        pygame.display.update()
        if x == 0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        if mouse_x <= corner1[0]:
                            while y == 0:
                                DISPLAYSURF.fill(WHITE)
                                DISPLAYSURF.blit(check, checkrect)
                                DISPLAYSURF.blit(males, malesrect)
                                DISPLAYSURF.blit(no, norect)
                                DISPLAYSURF.blit(yes, yesrect)
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_x <= corner1[0]:
                                                G[2] = 'Male'
                                                x = 1
                                                return
                                            elif mouse_x >= corner2[0]:
                                                y = 1
                                                
                                            
                        
                        elif mouse_x >= corner2[0]:
                            while y == 0:
                                DISPLAYSURF.fill(WHITE)
                                DISPLAYSURF.blit(check, checkrect)
                                DISPLAYSURF.blit(females, femalesrect)
                                DISPLAYSURF.blit(no, norect)
                                DISPLAYSURF.blit(yes, yesrect)
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_x <= corner1[0]:
                                                G[2] = 'Female'
                                                x = 1
                                                return
                                            elif mouse_x >= corner2[0]:
                                                y = 1
        elif x == 1:
            break
	




