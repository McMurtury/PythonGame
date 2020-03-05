import pygame, sys, textwrap, Image_dir, Class_list, Invent, Items, savingTest
from pygame.locals import *
from Image_dir import *
from Invent import *
from Items import *

pygame.init()

mouse_x = 0
mouse_y = 0

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Main')

player = Class_list.character ("player", 1, 1, 1, 1, 1, 1, 0, 0, 'none', 'none')
player.inventSize = 14

L = 0
def mainmenu(L):
    
    
    while True:
        screen.fill(Image_dir.SGRAY)
        screen.blit (Image_dir.ng, (300, 200))
        screen.blit (Image_dir.cg, (300, 275))
        #screen.blit (Image_dir.om, (300, 350))
        #screen.blit (Image_dir.cd, (300, 425))
        screen.blit (Image_dir.qt, (300, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_x > 300 and mouse_x < 500:
                        if mouse_y > 200 and mouse_y < 250:
                            characterCreation()
                            L = 1
                            
                            
                        if mouse_y > 275 and mouse_y < 325:
                            savingTest.con(player)
                        #if mouse_y > 350 and mouse_y < 400:

                        #if mouse_y > 425 and mouse_y < 475:

                        if mouse_y > 500 and mouse_y < 550:
                            pygame.quit()
                            sys.exit()
        if L == 1:
            break
    return L
    
        



    
def characterCreation():
    gender()
    classSelection()
    statAsginment()
    name()
    confrimCh()
    player.inventSize = 14
    savingTest.save(player)
    
def gender ():
    x = 0
    while True:
        screen.fill(Image_dir.LSBLUE)
        screen.blit(Image_dir.male, (0, 200))
        screen.blit (Image_dir.female, (400, 200))
        screen.blit (Image_dir.genderSelect, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_y > 200:
                        if mouse_x < 400:
                            player.gender = "Male"
                            x = 1
                            return
                        elif mouse_x > 400:
                            player.gender = "Female"
                            x = 1
                            return
        if x == 1:
            break

def classSelection ():
    x = 0
    while True:
        c = 0
        screen.blit (Image_dir.startingClass, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_y > 150:
                        if mouse_x < 250:
                            screen.blit (Image_dir.chWarrior, (0,0))
                            screen.blit (Image_dir.yesi, (130, 540))
                            screen.blit (Image_dir.noi, (570, 540))
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_y > 540 and mouse_y < 590:
                                                if mouse_x > 130 and mouse_x < 230:
                                                    player.clas = 'Warrior'
                                                    x = 1
                                                    return
                                                elif mouse_x > 570 and mouse_x < 670:
                                                    c = 1
                                if c == 1:
                                    break
                                            
                        elif mouse_x > 275 and mouse_x < 525:
                            screen.blit (Image_dir.chThief, (0,0))
                            screen.blit (Image_dir.yesi, (130, 540))
                            screen.blit (Image_dir.noi, (570, 540))
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_y > 540 and mouse_y < 590:
                                                if mouse_x > 130 and mouse_x < 230:
                                                    player.clas = 'Thief'
                                                    x = 1
                                                    return
                                                elif mouse_x > 570 and mouse_x < 670:
                                                    c = 1
                                if c == 1:
                                    break
                                            
                        elif mouse_x > 550:
                            screen.blit (Image_dir.chMage, (0,0))
                            screen.blit (Image_dir.yesi, (130, 540))
                            screen.blit (Image_dir.noi, (570, 540))
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            mouse_x, mouse_y = event.pos
                                            if mouse_y > 540 and mouse_y < 590:
                                                if mouse_x > 130 and mouse_x < 230:
                                                    player.clas = 'Mage'
                                                    x = 1
                                                    return
                                                elif mouse_x > 570 and mouse_x < 670:
                                                    c = 1
                                if c == 1:
                                    break
                        
        if x == 1:
            break

def statAsginment():
    x = 0
    p = 18

    player.magic = 1
    player.agility = 1
    player.intell = 1
    player.strength = 1
    player.endurance = 1
    player.sramina = 1
    
    fontObj = pygame.font.Font(None, 40)
    confrim = fontObj.render('Are you sure?', True, Image_dir.BLACK)
    
    while True:
        c = 0
        remain = fontObj.render(str(p), True, Image_dir.BLACK)
        mag = fontObj.render(str(player.magic), True, Image_dir.BLACK)
        ag = fontObj.render(str(player.agility), True, Image_dir.BLACK)
        Int = fontObj.render(str(player.intell), True, Image_dir.BLACK)
        Str = fontObj.render(str(player.strength), True, Image_dir.BLACK)
        End = fontObj.render(str(player.endurance), True, Image_dir.BLACK)
        sta = fontObj.render(str(player.stamina), True, Image_dir.BLACK)
        screen.blit (Image_dir.attribute, (0,0))
        screen.blit (remain, (528, 85))
        screen.blit (mag, (50, 240))
        screen.blit (ag, (161, 240))
        screen.blit (Int, (278, 240))
        screen.blit (Str, (418, 240))
        screen.blit (End, (563, 240))
        screen.blit (sta, (705, 240))
        if p == 18:
            screen.blit (Image_dir.bar, (0, 279))
        if p == 0:
            screen.blit (Image_dir.bar, (0, 175))
        if p == 0:
            screen.blit (confrim, (300, 475))
            screen.blit (Image_dir.yesi, (130, 540))
            screen.blit (Image_dir.noi, (570, 540))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_y > 175 and mouse_y < 225 and p > 0:
                        if mouse_x > 30 and mouse_x < 84:
                            player.magic = player.magic + 1
                            p = p-1
                        elif mouse_x > 140 and mouse_x < 194:
                            player.agility = player.agility + 1
                            p = p-1
                        elif mouse_x > 257 and mouse_x < 311:
                            player.intell = player.intell + 1
                            p = p-1
                        elif mouse_x > 398 and mouse_x < 452:
                            player.strength = player.strength + 1
                            p = p-1
                        elif mouse_x > 540 and mouse_x < 594:
                            player.endurance = player.endurance + 1
                            p = p-1
                        elif mouse_x > 684 and mouse_x < 738:
                            player.stamina = player.stamina + 1
                            p = p-1

                    elif mouse_y > 279 and mouse_y < 329:
                        if mouse_x > 30 and mouse_x < 84 and player.magic != 1:
                            player.magic = player.magic - 1
                            p = p + 1
                        elif mouse_x > 140 and mouse_x < 194 and player.agility != 1:
                            player.agility = player.agility - 1
                            p = p + 1
                        elif mouse_x > 257 and mouse_x < 311 and player.intell != 1:
                            player.intell = player.intell - 1
                            p = p + 1
                        elif mouse_x > 398 and mouse_x < 452 and player.strength != 1:
                            player.strength = player.strength - 1
                            p = p + 1
                        elif mouse_x > 540 and mouse_x < 594 and player.endurance != 1:
                            player.endurance = player.endurance - 1
                            p = p + 1
                        elif mouse_x > 684 and mouse_x < 738 and player.stamina != 1:
                            player.stamina = player.stamina - 1
                            p = p + 1

                    if p == 0:
                        if mouse_y > 540 and mouse_y < 590:
                            if mouse_x > 130 and mouse_x < 230:
                                player.maxhp = player.endurance*player.endurance*4
                                player.maxsp = player.stamina*player.stamina*player.endurance
                                player.maxmp = player.magic*player.magic*player.intell
                                return
                            
                            
def name():
    fontObj = pygame.font.Font(None, 40)
    check = fontObj.render('Are you sure?', True, Image_dir.SGRAY)
    nameq = fontObj.render('What is your name?', True, Image_dir.SGRAY)
    namerect = check.get_rect()
    namerect.center = (300, 100)
    x = 1
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    player.name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    player.name = player.name[:-1]
                elif evt.key == K_RETURN:
                    player.name = player.name
                    x = 0                    
            elif evt.type == QUIT:
                 return
        
        screen.fill(Image_dir.LSBLUE)
        screen.blit(nameq, namerect)
        block = font.render(player.name, True, Image_dir.NAVY)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
        
        if x == 0:
            
            break

def confrimCh():
    fontObj = pygame.font.Font(None, 50)
    fon = pygame.font.Font(None, 60)

    mag = fontObj.render(str(player.magic), True, Image_dir.BLACK)
    ag = fontObj.render(str(player.agility), True, Image_dir.BLACK)
    Int = fontObj.render(str(player.intell), True, Image_dir.BLACK)
    Str = fontObj.render(str(player.strength), True, Image_dir.BLACK)
    End = fontObj.render(str(player.endurance), True, Image_dir.BLACK)
    sta = fontObj.render(str(player.stamina), True, Image_dir.BLACK)

    nam = fon.render(player.name, True, Image_dir.DGREEN)
    gen = fon.render(player.gender, True, Image_dir.DGREEN)
        
    if player.clas == 'Warrior':
        screen.blit(Image_dir.confrimWarrior, (0,0))
    if player.clas == 'Thief':
        screen.blit(Image_dir.confrimThief, (0,0))
    if player.clas == 'Mage':
        screen.blit(Image_dir.confrimMage, (0,0))
    screen.blit(nam, (215, 35))
    screen.blit(gen, (253, 101))
    screen.blit(mag, (303, 253))
    screen.blit(ag, (303, 308))
    screen.blit(Int, (303, 362))
    screen.blit(Str, (303, 417))
    screen.blit(End, (303, 473))
    screen.blit(sta, (303, 528))
    pygame.display.update()
    z = 0
    while True:
        if z == 1:
            return
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_y > 539 and mouse_y < 589:
                        if mouse_x > 375 and mouse_x < 475:
                            z = 1
                        if mouse_x > 518 and mouse_x < 618:
                            characterCreation()
        
                            


def gameStart():
    fontObj = pygame.font.Font(None, 30)
    screen.fill(Image_dir.SGRAY)
    
    with open ('Text\Intro.txt', 'r') as f:
         data = f.readlines()
         for line in data:
              temp = line
    i = 0
    text = textwrap.wrap(temp, 60)
    while True:
        test = fontObj.render(text[i], True, BLACK)
        screen.blit (test, (75, (75 + (i*25))))
        pygame.display.update()
        i = i + 1
        if i == (len(text)):
            break
    while True:
        c = 0
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_y > 0 and mouse_x > 0:
                        c = 1
        if c != 0:
            break
    
    


i = 0

while True:
    
    player.inventP.append(Items.heatlhP)
    i+=1
    if i==3:
        i=0
        break
while True:
    
    player.inventP.append(Items.staminaP)
    i+=1
    if i==3:
        i=0
        break
while True:
    
    player.inventP.append(Items.manaP)
    i+=1
    if i==3:
        i=0
        break


L = mainmenu(L)
#print player.maxhp
#print player.maxsp
#print player.maxmp
#print L
#if L == 1:
#    gameStart()
#Invent.displayInven(player)

pygame.quit()
sys.exit()

