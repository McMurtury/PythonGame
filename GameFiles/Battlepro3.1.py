import pygame, sys
from pygame.locals import *
from random import randrange

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Battle Protype')

mouse_x = 0
mouse_y = 0

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#imported varibles from test program. Not final ones.

class attack ():
     def__init__(self, name ,element , attType, archType, spCost, mpCost, image):
         self.name = name
         self.element
         self.attType
         self.archType
         self.spCost
         self.mpCost
         self.image

slash = attack ("Slash", "none", 0, 0, 5, 0, pygame.image.load('attack_One.png'))

mp = 0
sp = 0
hdam = 0

# list properties:
# Health, Mana, Stamina, Defense, Dodfe, Speed, Crit, Meldam, Rangedam, Magicdam
# Weakness, Elemental weakness, attack type, attack element, target, attack archtype, image

battle = [100,100,100,2,0,4,25,6,6,5,1,"f",0,"n",0,0,0]
abattle = [100,100,100,2,0,4,25,6,6,5,1,"a",0,"n",0,0,0]
aabattle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aaabattle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

ebattle = [50,0,0,1,15,7,20,20,5,5,1,"if",0,"a",0,0,0]
eebattle = [50,0,0,1,15,5,20,20,5,5,0,"if",0,"n",0,0,0]
eeebattle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
eeeebattle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#images for battle.
battle[16] = pygame.image.load('player.png')
abattle[16] = pygame.image.load('allyi.png')
aabattle[16] = pygame.image.load('allyii.png')
aaabattle[16] = pygame.image.load('allyiii.png')

attackOne = pygame.image.load('Attack_One.png')

ebattle[16] = pygame.image.load('enemyi.png')
eebattle[16] = pygame.image.load('enemyii.png')
eeebattle[16] = pygame.image.load('enemyiii.png')
eeeebattle[16] = pygame.image.load('enemyiv.png')

background = pygame.image.load('Wood.png')
sideMenu = pygame.image.load('sideMenu.png')
terrain = pygame.image.load('terrain.png')
weather = pygame.image.load('weather.png')
border = pygame.image.load('battleBorder.png')

i = 0

def enemyAttack(E):
    
    while True:
        target = randrange(0 , 40);
        print target
        attackType = randrange(0 , 1);
        print attackType
        E[12] = str(attackType)

        if attackType < 2: #If the attack isn't a healing skill.
            if target <= 10 and battle[0]>0:
                E[14] = battle
                break
            elif target > 10 and target <=20 and abattle[0]>0:
                E[14] = abattle
                break
            elif target > 20 and target <=30 and aabattle[0]>0:
                E[14] = aabattle
                break
            elif target > 30 and target <=40 and aaabattle[0]>0:
                E[14] = aaabattle
                break

        elif attackType >2: #if the attack is a healing skill.
            if target <= 10 and target > 0 and ebattle[0]<80:
                E[14] = ebattle
                break
            elif target > 10 and target <=20 and eebattle[0]>0 and eebattle[0]<80:
                E[14] = eebattle
                break
            elif target > 20 and target <=30 and eeebattle[0]>0 and eeebattle[0]<80:
                E[14] = eeebattle
                break
            elif target > 30 and target <=40 and eeeebattle[0]>0 and eeeebattle[0]<80:
                E[14] = eeeebattle
                break


screen.blit (background, (100, 0))
screen.blit (sideMenu, (0, 0))
screen.blit (terrain, (450 , 180))
screen.blit (weather, (450 , 320))
screen.blit (attackOne, (20, 50))
screen.blit (attackOne, (20, 154))
screen.blit (attackOne, (20, 258))
screen.blit (attackOne, (20, 362))
screen.blit (attackOne, (20, 466))

def playerCards ():
    if battle[0] > 0:
        tph = 100 #Total health
        tmp = 100 #mana
        tsp = 100 #stamina
        hdam = tph - battle[0]
        mdrain = tmp - battle[1]
        sdrain = tsp - battle[2]
    
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)

        bmp = tmp - mdrain
        per = bmp/float(tmp)
        mp = per*100
    
        bmp = tsp - sdrain
        per = bmp/float(tsp)
        sp = per*100

        screen.blit (battle[16], (250, 40))
        pygame.draw.rect (screen, BLUE, (228, (40+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (40+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (141-hdam), 100, hdam))
        screen.blit (border, (220 , 33))

    if abattle[0] > 0:
        tph = 100 #Total health
        tmp = 100 #mana
        tsp = 100 #stamina
        hdam = tph - abattle[0]
        mdrain = tmp - abattle[1]
        sdrain = tsp - abattle[2]

        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)

        bmp = tmp - mdrain
        per = bmp/float(tmp)
        mp = per*100

        bmp = tsp - sdrain
        per = bmp/float(tsp)
        sp = per*100

        screen.blit (abattle[16], (250, 180))
        pygame.draw.rect (screen, BLUE, (228, (180+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (180+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (281-hdam), 100, hdam))
        screen.blit (border, (220 , 173))

    if aabattle[0] > 0:
        tph = 100 #Total health
        tmp = 100 #mana
        tsp = 100 #stamina
        hdam = tph - aabattle[0]
        mdrain = tmp - aabattle[1]
        sdrain = tsp - aabattle[2]
    
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)
        
        bmp = tmp - mdrain
        per = bmp/float(tmp)
        mp = per*100
    
        bmp = tsp - sdrain
        per = bmp/float(tsp)
        sp = per*100
    
        screen.blit (aabattle[16], (250, 320))
        pygame.draw.rect (screen, BLUE, (228, (320+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (320+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (421-hdam), 100, hdam))
        screen.blit (border, (220 , 313))
    
    if aaabattle[0] > 0:
        tph = 100 #Total health
        tmp = 100 #mana
        tsp = 100 #stamina
        hdam = tph - aaabattle[0]
        mdrain = tmp - aaabattle[1]
        sdrain = tsp - aaabattle[2]
    
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)
        
        bmp = tmp - mdrain
        per = bmp/float(tmp)
        mp = per*100
    
        bmp = tsp - sdrain
        per = bmp/float(tsp)
        sp = per*100
        
        screen.blit (aaabattle[16], (250, 460))
        pygame.draw.rect (screen, BLUE, (228, (460+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (460+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (561-hdam), 100, hdam))
        screen.blit (border, (220 , 453))

def enemyCards ():
    if ebattle[0] >0:
        tph = 50
        hdam = tph - ebattle[0]
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)
        screen.blit (ebattle[16], (650, 40))
        pygame.draw.rect(screen, RED, (650, (141-hdam), 100, hdam))
        
    if eebattle[0] >0:
        tph = 50
        hdam = tph - eebattle[0]
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)
        screen.blit (eebattle[16], (650, 180))
        pygame.draw.rect(screen, RED, (650, (281-hdam), 100, hdam))
        
    if eeebattle[0] >0:
        tph = 50
        hdam = tph - eeebattle[0]
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)
        screen.blit (eeebattle[16], (650, 320))
        pygame.draw.rect(screen, RED, (650, (421-hdam), 100, hdam))
        
    if eeeebattle[0] >0:
        tph = 50
        hdam = tph - eeeebattle[0]
        bph = tph - hdam
        per = bph/float(tph)
        hdam = 100-(per*100)
        screen.blit (eeeebattle[16], (650, 460))
        pygame.draw.rect(screen, RED, (650, (561-hdam), 100, hdam))


playerCards()
enemyCards()
pygame.display.update()
"""raw_input()
battle[0] = battle[0] - 15
playerCards()
enemyCards()
pygame.display.update()
"""

# Sorts based on speed with the highest first.
fightOrder = sorted([battle, ebattle, eebattle, eeebattle, eeeebattle, abattle, aabattle, aaabattle], key = lambda x: x[5], reverse=True)

def target (T):
    t = 0
    while t == 0:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 40 and mouse_y <= 140:
                        T[14] = ebattle
                        t = 1
                    elif mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 180 and mouse_y <= 280:
                        T[14] = eebattle
                        t = 1

def move (T):
    m = 0
    while m == 0:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 40 and mouse_y <= 140:
                        
                        m = 1
                    elif mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 180 and mouse_y <= 280:
                        
                        m = 1

z = randrange(1, 100);
h = randrange(1, 100);

if battle[0] > 0:
    target(battle)

if abattle[0] >0:
    target(abattle)

if ebattle[0]>0:
    enemyAttack(ebattle)
    
            
if eebattle[0]>0:
    enemyAttack(eebattle)
    
            
for i in range(len(fightOrder)):
    if fightOrder[i][0]>0:
        if fightOrder[i][14][4] > h:
            print "Dodged!"
        else:
            print "Getting something. Maybe"
            if fightOrder[i][12] == fightOrder[i][14][10] or str(fightOrder[i][13]) in str(fightOrder[i][14][11]):
                if fightOrder[i][6] >= z:
                    print "Weakness + crit!"
                    if fightOrder[i][15] == 0: #melee attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][7]/fightOrder[i][14][3]) * 6)
                    elif fightOrder[i][15] == 1: #magic attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][9]/fightOrder[i][14][3]) * 6)
                    elif fightOrder[i][15] == 2: #range attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][8]/fightOrder[i][14][3]) * 6)
                else:
                    print "Weakness"
                    if fightOrder[i][15] == 0: #melee attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][7]/fightOrder[i][14][3]) * 2)
                    elif fightOrder[i][15] == 1: #magic attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][9]/fightOrder[i][14][3]) * 2)
                    elif fightOrder[i][15] == 2: #range attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][8]/fightOrder[i][14][3]) * 2)

            else:
                if fightOrder[i][6] >= z:
                    print "Crit!"
                    if fightOrder[i][15] == 0: #melee attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][7]/fightOrder[i][14][3]) * 3)
                    elif fightOrder[i][15] == 1: #magic attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][9]/fightOrder[i][14][3]) * 3)
                    elif fightOrder[i][15] == 2: #range attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][8]/fightOrder[i][14][3]) * 3)
                else:
                    if fightOrder[i][15] == 0: #melee attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - (fightOrder[i][7]/fightOrder[i][14][3])
                    elif fightOrder[i][15] == 1: #magic attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - (fightOrder[i][9]/fightOrder[i][14][3])
                    elif fightOrder[i][15] == 2: #range attack.
                        fightOrder[i][14][0] = fightOrder[i][14][0] - (fightOrder[i][8]/fightOrder[i][14][3])

    
print battle[0]
print abattle[0]
playerCards()
enemyCards()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
