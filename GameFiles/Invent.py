import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Inventory Protype')

mouse_x = 0
mouse_y = 0

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
PURPLE = (160, 32, 240)
NAVY = (0, 0, 255)
SGRAY = (49, 79, 79)
BLACK = (0, 0, 0)
LGRAY = (211, 211, 211)
CYAN = (0, 255, 255)
LSBLUE = (176, 196, 222)
DGREEN = (0, 100, 0)
LSGREEN = (32, 178, 170)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
IRED = (205, 92,92)
SIENNA = (160, 82, 45)
FIREBRICK = (178, 34, 34)
DPINK = (255, 20, 146)
LPINK = (255, 182, 193)
ORCHID = (218, 112, 214)


def inventDisplayP(player):
    screen.fill (DGREEN)
    screen.blit (potionh, (0, 200))
    screen.blit (armorh, (200, 200))
    screen.blit (weaponsh, (400, 200))
    screen.blit (questh, (600, 200)) 
    screen.blit (lighten, (0, 200))
    screen.blit (retur, (701, 0))
    screen.blit (use, (701, 50))
    screen.blit (drop, (701, 100))
    screen.blit (sort, (701, 150))
    
    i = 0
    j = 0
    while True:
        if i<len(player.inventP):
            screen.blit (player.inventP[i].icon, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1
        elif i<player.inventSize:
            screen.blit (emp, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1             
        elif i<28:
            screen.blit (unava, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1                          
        else:
            screen.blit (overlay, (0, 0))
            pygame.display.update()
            i=0
            break

def inventDisplayA(player):
    screen.fill (DGREEN)
    screen.blit (potionh, (0, 200))
    screen.blit (armorh, (200, 200))
    screen.blit (weaponsh, (400, 200))
    screen.blit (questh, (600, 200)) 
    screen.blit (lighten, (200, 200))
    screen.blit (retur, (701, 0))
    screen.blit (use, (701, 50))
    screen.blit (drop, (701, 100))
    screen.blit (sort, (701, 150))
    
    i = 0
    j = 0
    while True:
        if i<len(player.inventA) and i<28:
            screen.blit (player.inventA[i].icon, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1
        elif i<player.inventSize:
            screen.blit (emp, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1             
        elif i<28:
            screen.blit (unava, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1                          
        else:
            screen.blit (overlay, (0, 0))
            pygame.display.update()
            i=0
            break         


def inventDisplayW(player):
    screen.fill (DGREEN)
    screen.blit (potionh, (0, 200))
    screen.blit (armorh, (200, 200))
    screen.blit (weaponsh, (400, 200))
    screen.blit (questh, (600, 200))
    screen.blit (lighten, (400, 200))
    screen.blit (retur, (701, 0))
    screen.blit (use, (701, 50))
    screen.blit (drop, (701, 100))
    screen.blit (sort, (701, 150))
    
    i = 0
    j = 0
    while True:
        if i<len(player.inventW) and i<28:
            screen.blit (player.inventW[i].icon, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1
        elif i<player.inventSize:
            screen.blit (emp, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1             
        elif i<28:
            screen.blit (unava, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1                          
        else:
            screen.blit (overlay, (0, 0))
            pygame.display.update()
            i=0
            break         


def inventDisplayQ(player):
    screen.fill (DGREEN)
    screen.blit (potionh, (0, 200))
    screen.blit (armorh, (200, 200))
    screen.blit (weaponsh, (400, 200))
    screen.blit (questh, (600, 200)) 
    screen.blit (lighten, (600, 200))
    screen.blit (retur, (701, 0))
    screen.blit (use, (701, 50))
    screen.blit (drop, (701, 100))
    screen.blit (sort, (701, 150))
    
    i = 0
    j = 0
    while True:
        if i<len(player.inventQ):
            screen.blit (player.inventQ[i].icon, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1
        elif i<player.inventSize:
            screen.blit (emp, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1             
        elif i<28:
            screen.blit (unava, (0+(200*(i-(j*4))), 250+(50*j)))
            i+=1
            if i%4==0:
                j+=1                          
        else:
            screen.blit (overlay, (0, 0))
            pygame.display.update()
            i=0
            break         
     
def hilight(x, y):
    if x<200:
         if y < 300:
              screen.blit (lighten, (0, 250))

         elif y >300 and y <350:
              screen.blit (lighten, (0, 300))

         elif y >350 and y <400:
              screen.blit (lighten, (0, 350))

         elif y >400 and y <450:
              screen.blit (lighten, (0, 400))

         elif y >450 and y <500:
              screen.blit (lighten, (0, 450))

         elif y >500 and y <550:
              screen.blit (lighten, (0, 500))

         elif y >550:
              screen.blit (lighten, (0, 550))
          
    elif x < 400:
         if y < 300:
              screen.blit (lighten, (200, 250))

         elif y >300 and y <350:
              screen.blit (lighten, (200, 300))

         elif y >350 and y <400:
              screen.blit (lighten, (200, 350))

         elif y >400 and y <450:
              screen.blit (lighten, (200, 400))

         elif y >450 and y <500:
              screen.blit (lighten, (200, 450))

         elif y >500 and y <550:
              screen.blit (lighten, (200, 500))

         elif y >550:
              screen.blit (lighten, (200, 550))

    elif x < 600:
         if y < 300:
              screen.blit (lighten, (400, 250))

         elif y >300 and y <350:
              screen.blit (lighten, (400, 300))

         elif y >350 and y <400:
              screen.blit (lighten, (400, 350))

         elif y >400 and y <450:
              screen.blit (lighten, (400, 400))

         elif y >450 and y <500:
              screen.blit (lighten, (400, 450))

         elif y >500 and y <550:
              screen.blit (lighten, (400, 500))

         elif y >550:
              screen.blit (lighten, (400, 550))

    else:
         if y < 300:
              screen.blit (lighten, (600, 250))

         elif y >300 and y <350:
              screen.blit (lighten, (600, 300))

         elif y >350 and y <400:
              screen.blit (lighten, (600, 350))

         elif y >400 and y <450:
              screen.blit (lighten, (600, 400))

         elif y >450 and y <500:
              screen.blit (lighten, (600, 450))

         elif y >500 and y <550:
              screen.blit (lighten, (600, 500))

         elif y >550:
              screen.blit (lighten, (600, 550))

    screen.blit (overlay, (0, 0)) 
    pygame.display.update()

def selector(player):
    i = 0 
    ii = 0
    p = 0
    while True:
        
        for event in pygame.event.get():
             if event.type == MOUSEBUTTONDOWN:
                  if event.button == 1:
                       mouse_x, mouse_y = event.pos
                       if mouse_x < 200 and mouse_y >= 200 and mouse_y < 250 and mouse_y > 200:
                            inventDisplayP(player)
                            p = 0
                       if mouse_x > 200 and mouse_x < 400 and mouse_y >= 200 and mouse_y < 250:
                            inventDisplayA(player)
                            p = 1
                       if mouse_x > 400 and mouse_x < 600 and mouse_y >= 200 and mouse_y < 250:
                            inventDisplayW(player)
                            p = 2
                       if mouse_x > 600 and mouse_x < 800 and mouse_y >= 200 and mouse_y < 250:
                            inventDisplayQ(player)
                            p = 3
                       if mouse_x > 700 and mouse_x < 800 and mouse_y < 100:
                            return
                         
                       elif mouse_y > 250:
                            i = 0
                            if p == 0:
                                 inventDisplayP(player)
                            if p == 1:
                                 inventDisplayA(player)
                            if p == 2:
                                 inventDisplayW(player)
                            if p == 3:
                                 inventDisplayQ(player)
                                 
                            if mouse_x > 200 and mouse_x < 400 and mouse_y > 250:
                                 i+=1
                            if mouse_x > 400 and mouse_x < 600 and mouse_y > 250:
                                 i+=2
                            if mouse_x > 600 and mouse_y > 250:
                                 i+=3
                            if mouse_y > 300 and mouse_y < 350:
                                 i+=4
                            if mouse_y > 350 and mouse_y < 400:
                                 i+=8
                            if mouse_y > 400 and mouse_y < 450:
                                 i+=12
                            if mouse_y > 450 and mouse_y < 500:
                                 i+=16
                            if mouse_y > 500 and mouse_y < 550:
                                 i+=20
                            if mouse_y > 550:
                                 i+=24
                            ii = i
                            if p == 0:
                                 if len(player.inventP) > ii:
                                      screen.blit (player.inventP[ii].image, (0, 0))
                            #print ii
                            if ((p == 0 or p == 3) and ii < player.inventSize) or ((p == 1 or p == 2) and ii < player.inventSize*2):
                                 hilight(mouse_x, mouse_y)
                            
                            
overlay = pygame.image.load('Inventory.png')
#healthPotion = pygame.image.load('health_potion.png')
#manaPotion = pygame.image.load('mana_potion.png')
#staminaPotion = pygame.image.load('stamina_potion.png')
potionh = pygame.image.load('potion.png')
questh = pygame.image.load('quest_items.png')
armorh = pygame.image.load('armor.png')
weaponsh = pygame.image.load('weapons.png')
lighten = pygame.image.load('lighten.png')
emp = pygame.image.load('empty.png')
unava = pygame.image.load('unava.png')
retur = pygame.image.load('return.png')
use = pygame.image.load('use.png')
drop = pygame.image.load('drop.png')
sort = pygame.image.load('sort.png')



def displayInven (player):
     inventDisplayP(player)
     selector(player)


#screen.fill (DGREEN)
#screen.blit (potionh, (0, 200))
#screen.blit (armorh, (200, 200))
#screen.blit (weaponsh, (400, 200))
#screen.blit (questh, (600, 200))
#inventDisplayP()
#screen.blit (lighten, (200, 250))
#screen.blit (healthPotion, (0, 250))
#screen.blit (manaPotion, (200, 250))
#screen.blit (staminaPotion, (400, 250))
#screen.blit (overlay, (0, 0))
#pygame.display.update()
#selector()

"""

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
"""
