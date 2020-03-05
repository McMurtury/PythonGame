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

def enemyAttack(E):
    
    while True:
         target = randrange(0 , 40);
         move = randrange (0, 1);
         if move == 0 and E[0].sp > E[0].attackOne.spCost and E[0].mp > E[0].attackOne.mpCost:
              E[1] = E[0].attackOne
         elif move == 1 and E[0].sp > E[0].attackTwo.spCost and E[0].mp > E[0].attackTwo.mpCost:
              E[1] = E[0].attackTwo

         if E[1].heal == 0:
              if target <= 10 and pOne != 0 and pOne[0].hp > 0:
                   E[2] = pOne[0]
                   break
              elif target < 10 and target <= 20 and pTwo !=0 and pTwo[0].hp > 0:
                   E[2] = pTwo[0]
                   break
              elif target < 20 and target <= 30 and pThree !=0 and pThree[0].hp > 0:
                   E[2] = pThree[0]
                   break
              elif target < 30 and target <= 40 and pFour !=0 and pFour[0].hp > 0:
                   E[2] = pFour[0]
                   break
         else:
              if target <= 10 and eOne != 0 and eOne[0].hp < 80:
                   E[2] = eOne[0]
                   break
              elif target < 10 and target <= 20 and eTwo !=0 and eTwo[0].hp > 0 and eTwo[0].hp < 80:
                   E[2] = eTwo[0]
                   break
              elif target < 20 and target <= 30 and eThree !=0 and eThree[0].hp > 0 and eThree[0].hp < 80:
                   E[2] = eThree[0]
                   break
              elif target < 30 and target <= 40 and eFour !=0 and eFour[0].hp > 0 and eFour[0].hp < 80:
                   E[2] = eFour[0]
                   break               

def target (T):
    t = 0
    while t == 0:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 40 and mouse_y <= 140 and enemOne.hp > 0:
                        T[2] = eOne[0]
                        t = 1
                    elif mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 180 and mouse_y <= 280 and eTwo[0] != 0 and eTwo[0].hp > 0:
                        T[2] = eTwo[0]
                        t = 1
                    elif mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 320 and mouse_y <= 420 and eThree[0] != 0 and eThree[0].hp > 0:
                        T[2] = eThree[0]
                        t = 1
                    elif mouse_x >= 650 and mouse_x <= 750 and mouse_y >= 460 and mouse_y <= 560 and eFour[0] != 0 and eFour[0].hp > 0:
                        T[2] = eFour[0]
                        t = 1

def move (M):
    m = 0
    screen.blit (M[0].attackOne.image, (20, 50))
    screen.blit (M[0].attackTwo.image, (20, 154))
    screen.blit (M[0].attackThree.image, (20, 258))
    screen.blit (M[0].attackFour.image, (20, 362))
    screen.blit (M[0].item.image, (20, 466))
    pygame.display.update()
    while m == 0:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if mouse_x >= 20 and mouse_x <= 180 and mouse_y >= 50 and mouse_y <= 134 and M[0].sp > M[0].attackOne.spCost and M[0].mp > M[0].attackOne.mpCost:
                        M[1] = M[0].attackOne
                        m = 1
                    elif mouse_x >= 20 and mouse_x <= 180 and mouse_y >= 154 and mouse_y <= 238 and M[0].sp > M[0].attackTwo.spCost and M[0].mp > M[0].attackTwo.mpCost:
                        M[1] = M[0].attackTwo
                        m = 1
                    elif mouse_x >= 20 and mouse_x <= 180 and mouse_y >= 258 and mouse_y <= 342 and M[0].sp > M[0].attackThree.spCost and M[0].mp > M[0].attackThree.mpCost:
                        M[1] = M[0].attackThree
                        m = 1
                    elif mouse_x >= 20 and mouse_x <= 180 and mouse_y >= 362 and mouse_y <= 446 and M[0].sp > M[0].attackFour.spCost and M[0].mp > M[0].attackFour.mpCost:
                        M[1] = M[0].attackFour
                        m = 1

class character ():
     def __init__(self, name, maxhp, maxsp, maxmp, hp, sp, mp, defense, speed, dodgeChance, critChance, meleeDam, rangeDam, magicDam, weakness, image, attackOne, attackTwo, attackThree, attackFour, item):
          self.name = name
          self.maxhp = maxhp
          self.maxsp = maxsp
          self.maxmp = maxmp
          self.hp = hp
          self.sp = sp
          self.mp = mp
          self.defense = defense
          self.speed = speed
          self.dodgeChance = dodgeChance
          self.critChance = critChance
          self.meleeDam = meleeDam
          self.rangeDam = rangeDam
          self.magicDam = magicDam
          self.weakness = weakness
          self.image = image
          self.attackOne = attackOne
          self.attackTwo = attackTwo
          self.attackThree = attackThree
          self.attackFour = attackFour
          self.item = item

class enemy ():
     def __init__ (self, name, maxhp, maxsp, maxmp, hp, sp, mp, defense, speed, dodgeChance, critChance, meleeDam, rangeDam, magicDam, weakness, image, attackOne, attackTwo):
          self.name = name
          self.maxhp = maxhp
          self.maxsp = maxsp
          self.maxmp = maxmp
          self.hp = hp
          self.sp = sp
          self.mp = mp
          self.defense = defense
          self.speed = speed
          self.dodgeChance = dodgeChance
          self.critChance = critChance
          self.meleeDam = meleeDam
          self.rangeDam = rangeDam
          self.magicDam = magicDam
          self.weakness = weakness
          self.image = image
          self.attackOne = attackOne
          self.attackTwo = attackTwo
class attack ():
     def __init__(self, name ,element , attType, archType, spCost, mpCost, image, power, heal):
         self.name = name
         self.element = element
         self.attType = attType
         self.archType = archType
         self.spCost = spCost
         self.mpCost = mpCost
         self.image = image
         self.power = power
         self.heal = heal
class item ():
     def __init__ (self, name, image):
          self.name = name
          self.image = image

slash = attack ("Slash", "none", 0, 0, 10, 0, pygame.image.load('attack_One.png'), 5, 0)
fireball = attack ("Fireball", "fire", 3, 1, 0, 10, pygame.image.load('fireball.png'), 5, 0)
thrust = attack ("Thrust", "none", 1, 0, 10, 0 , pygame.image.load('thrust.png'), 5, 0)
throwAxe = attack ("Throwing Axe", "none", 1, 2, 10, 0, pygame.image.load('throwingAxe.png'), 5, 0)
heal = attack ("Heal", "none", 4, 1, 0, 20, pygame.image.load('heal.png'), 5, 1)

base = item ("nothing", pygame.image.load('item.png'))

player = character ("player", 100, 100, 100, 100, 100, 100, 10, 5, 30, 30, 20, 5, 5, ["null", 1], pygame.image.load('player.png'),slash, thrust, fireball, heal, base)

enem = enemy ("Enemy", 50, 50, 50, 50, 50, 50, 5, 7, 0, 30, 20,10,10, ["fire", 0], pygame.image.load('enemyi.png'), slash,thrust)
eBase = enemy ("Base emeny", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

enemOne = 0
enemTwo = 0
enemThree = 0
enemFour = 0

pOne = 0
pTwo = 0
pThree = 0
pFour = 0

eOne = 0
eTwo = 0
eThree = 0
eFour = 0

enemOne = enem


pOne = [player, 0, 0]
pTwo = [player, 0, 0]
pThree = [player, 0, 0]
pFour = [player, 0, 0]

eOne = [enemOne, 0, 0]
eTwo = [enemOne, 0, 0]
eThree = [enemOne, 0, 0]
eFour = [enemOne, 0, 0]

background = pygame.image.load('Wood.png')
sideMenu = pygame.image.load('sideMenu.png')
terrain = pygame.image.load('terrain.png')
weather = pygame.image.load('weather.png')
border = pygame.image.load('battleBorder.png')

i = 0

def playerCards ():
    if (player.hp > 0):
        hdam = player.maxhp - player.hp
        mdrain = player.maxmp - player.mp
        sdrain = player.maxsp - player.sp

        per = (player.maxhp - hdam)/float(player.maxhp)
        hdam = 100 - (per*100)

        per = (player.maxmp - mdrain)/float(player.maxmp)
        mp = per*100

        per = (player.maxsp - sdrain)/float(player.maxsp)
        sp = per*100

        screen.blit (player.image, (250, 40))
        pygame.draw.rect (screen, BLUE, (228, (40+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (40+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (141-hdam), 100, hdam))
        screen.blit (border, (220 , 33))
    if (pTwo[0].hp > 0):
        hdam = pTwo[0].maxhp - pTwo[0].hp
        mdrain = pTwo[0].maxmp - pTwo[0].mp
        sdrain = pTwo[0].maxsp - pTwo[0].sp

        per = (pTwo[0].maxhp - hdam)/float(pTwo[0].maxhp)
        hdam = 100 - (per*100)

        per = (pTwo[0].maxmp - mdrain)/float(pTwo[0].maxmp)
        mp = per*100

        per = (pTwo[0].maxsp - sdrain)/float(pTwo[0].maxsp)
        sp = per*100

        screen.blit (pTwo[0].image, (250, 180))
        pygame.draw.rect (screen, BLUE, (228, (180+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (180+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (281-hdam), 100, hdam))
        screen.blit (border, (220 , 173))
    if (pThree[0] != 0 and pThree[0].hp > 0):
        hdam = pThree[0].maxhp - pThree[0].hp
        mdrain = pThree[0].maxmp - pThree[0].mp
        sdrain = pThree[0].maxsp - pThree[0].sp

        per = (pThree[0].maxhp - hdam)/float(pThree[0].maxhp)
        hdam = 100 - (per*100)

        per = (pThree[0].maxmp - mdrain)/float(pThree[0].maxmp)
        mp = per*100

        per = (pThree[0].maxsp - sdrain)/float(pThree[0].maxsp)
        sp = per*100

        screen.blit (pThree[0].image, (250, 320))
        pygame.draw.rect (screen, BLUE, (228, (320+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (320+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (421-hdam), 100, hdam))
        screen.blit (border, (220 , 313))
    if (pFour[0] != 0 and pFour[0].hp > 0):
        hdam = pFour[0].maxhp - pFour[0].hp
        mdrain = pFour[0].maxmp - pFour[0].mp
        sdrain = pFour[0].maxsp - pFour[0].sp

        per = (pFour[0].maxhp - hdam)/float(pFour[0].maxhp)
        hdam = 100 - (per*100)

        per = (pFour[0].maxmp - mdrain)/float(pFour[0].maxmp)
        mp = per*100

        per = (pFour[0].maxsp - sdrain)/float(pFour[0].maxsp)
        sp = per*100

        screen.blit (pFour[0].image, (250, 460))
        pygame.draw.rect (screen, BLUE, (228, (460+(100-mp)), 14, mp))
        pygame.draw.rect (screen, GREEN, (358, (460+(100-sp)), 14, sp))
        pygame.draw.rect(screen, RED, (250, (561-hdam), 100, hdam))
        screen.blit (border, (220 , 453))

def enemyCards ():
    if (enemOne.hp > 0):
        hdam = enemOne.maxhp - enemOne.hp
        per = (enemOne.maxhp - hdam)/float(enemOne.maxhp)
        hdam = 100 - (per*100)
        screen.blit (enemOne.image, (650, 40))
        pygame.draw.rect(screen, RED, (650, (141-hdam), 100, hdam))
    if (eTwo[0] != 0 and eTwo[0].hp > 0):
        hdam = eTwo[0].maxhp - eTwo[0].hp
        per = (eTwo[0].maxhp - hdam)/float(eTwo[0].maxhp)
        hdam = 100 - (per*100)
        screen.blit (eTwo[0].image, (650, 180))
        pygame.draw.rect(screen, RED, (650, (281-hdam), 100, hdam))
    if (eThree[0] != 0 and eThree[0].hp > 0):
        hdam = eThree[0].maxhp - eThree[0].hp
        per = (eThree[0].maxhp - hdam)/float(eThree[0].maxhp)
        hdam = 100 - (per*100)
        screen.blit (eThree[0].image, (650, 320))
        pygame.draw.rect(screen, RED, (650, (421-hdam), 100, hdam))
    if (eFour[0] != 0 and eFour[0].hp > 0):
        hdam = eFour[0].maxhp - eFour[0].hp
        per = (eFour[0].maxhp - hdam)/float(eFour[0].maxhp)
        hdam = 100 - (per*100)
        screen.blit (eFour[0].image, (650, 460))
        pygame.draw.rect(screen, RED, (650, (561-hdam), 100, hdam))

while True:
    if (eOne[0] == 0 or eOne[0].hp <= 0) and (eTwo[0] == 0 or eTwo[0].hp <=0) and (eThree[0] == 0 or eThree[0].hp <= 0) and (eFour[0] == 0 or eFour[0].hp <= 0):
        print "Victory"
        break
    elif (pOne[0] == 0 or pOne[0].hp <= 0) and (pTwo[0] == 0 or pTwo[0].hp <= 0) and (pThree[0] == 0 or pThree[0].hp <= 0) and (pFour[0] == 0 or pFour[0].hp <= 0):
        print "Defeat"
        break
    
    screen.blit (background, (100, 0))
    screen.blit (sideMenu, (0, 0))
    screen.blit (terrain, (450 , 180))
    screen.blit (weather, (450 , 320))
    playerCards()
    enemyCards()
    pygame.display.update()

    move (pOne)
    target (pOne)


    eOne[1] = eOne[0].attackOne
    eOne[2] = pOne[0]
    eTwo[1] = eOne[0].attackOne
    eTwo[2] = pTwo[0]



    fightOrder = sorted([pOne, eOne], key = lambda x: x[0].speed, reverse=True)

    z = randrange(1, 100);
    h = randrange(1, 100);

    print pOne[1].name

    for i in range(len(fightOrder)):
        if fightOrder[i][0].hp > 0:
            print fightOrder[i][0].name
            fightOrder[i][0].sp = fightOrder[i][0].sp - fightOrder[i][1].spCost
            fightOrder[i][0].mp = fightOrder[i][0].mp - fightOrder[i][1].mpCost

            if fightOrder[i][2].dodgeChance < h:
                x = randrange(1, fightOrder[i][1].power)
                if fightOrder[i][1].attType in fightOrder[i][2].weakness or fightOrder[i][1].element in fightOrder[i][2].weakness:
                    if fightOrder[i][0].critChance >= z:
                        if fightOrder[i][1].archType == 0: #melee attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].meleeDam+x)/fightOrder[i][2].defense) * 6)
                        elif fightOrder[i][1].archType == 1: #magic attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].magicDam+x)/fightOrder[i][2].defense) * 6)
                        elif fightOrder[i][1].archType == 2: #range attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].rangeDam+x)/fightOrder[i][2].defense) * 6)
                    else:
                        if fightOrder[i][1].archType == 0: #melee attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].meleeDam+x)/fightOrder[i][2].defense) * 2)
                        elif fightOrder[i][1].archType == 1: #magic attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].magicDam+x)/fightOrder[i][2].defense) * 2)
                        elif fightOrder[i][1].archType == 2: #range attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].rangeDam+x)/fightOrder[i][2].defense) * 2)
                else:
                    if fightOrder[i][0].critChance >= z:
                        if fightOrder[i][1].archType == 0: #melee attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].meleeDam+x)/fightOrder[i][2].defense) * 3)
                        elif fightOrder[i][1].archType == 1: #magic attack
                            if fightOrder[i][1].heal == 1:
                                fightOrder[i][2].hp = fightOrder[i][2].hp + ((fightOrder[i][0].magicDam+x) * 3)
                            else:
                                fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].magicDam+x)/fightOrder[i][2].defense) * 3)
                        elif fightOrder[i][1].archType == 2: #range attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - (((fightOrder[i][0].rangeDam+x)/fightOrder[i][2].defense) * 3)
                    else:
                        if fightOrder[i][1].archType == 0: #melee attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - ((fightOrder[i][0].meleeDam+x)/fightOrder[i][2].defense)
                        elif fightOrder[i][1].archType == 1: #magic attack
                            if fightOrder[i][1].heal == 1:
                                fightOrder[i][2].hp = fightOrder[i][2].hp + (fightOrder[i][0].magicDam+x)
                            else:
                                fightOrder[i][2].hp = fightOrder[i][2].hp - ((fightOrder[i][0].magicDam+x)/fightOrder[i][2].defense)
                        elif fightOrder[i][1].archType == 2: #range attack
                            fightOrder[i][2].hp = fightOrder[i][2].hp - ((fightOrder[i][0].rangeDam+x)/fightOrder[i][2].defense)




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
