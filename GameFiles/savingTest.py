import pygame, sys, Image_dir, Class_list, Items, glob
from pygame.locals import *
from Image_dir import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Saving')
SGRAY = (49, 79, 79)

mouse_x = 0
mouse_y = 0


def save(player):
    file = open('Saves/'+player.name+".txt" , "w")
    file.write(player.name + " " + str(player.magic) + " " + str(player.agility) + " " \
               + str(player.strength) + " " + str(player.intell) + " " + str(player.endurance)\
                + " " + str(player.stamina) + " " + str(player.maxhp) +" "+ str(player.maxsp) +" "+ str(player.maxmp) \
               +" "+ str(player.hp) + " " + str(player.sp) + " "\
               +str(player.mp) + " " + str(player.inventSize) + " " \
               +str(player.gold) + " " + str(player.gender) + " " + str(player.clas))
    
    
    file.close()

def read(fil, player):
    with open (fil, 'r') as f:
         data = f.readlines()
         for line in data:
              temp = line.split()
              
         player.name = temp[0]
         player.magic = temp[1]
         player.agility = temp[2]
         player.strength = temp[3]
         player.intell = temp[4]
         player.endurance = temp[5]
         player.stamina = temp[6]
         player.hp = temp[7]
         player.sp = temp[8]
         player.mp = temp[9]
         player.inventSize = temp[10]
         player.inventP = temp[11]
         player.inventA = temp[12]
         player.inventW = temp[13]
         player.inventQ = temp[14]
         player.gold = temp[15]
         player.gender = temp[16]
         player.clas = temp[17]
         
    print file.readlines()
    
def con(player):
     screen.fill (Image_dir.DGREEN)
     pygame.display.update()
     
     temp = []
     temp = (glob.glob("Saves/*.txt"))
     i = len(temp)
     print i
     fontObj = pygame.font.Font(None, 40)
     noSave = fontObj.render('NO SAVE DATA', True, Image_dir.BLACK)
     
     #pygame.draw.rect (screen, SGRAY (100, 100, 500, 100))
     #pygame.draw.rect (screen, SGRAY (100, 275, 500, 100))
     #pygame.draw.rect (screen, SGRAY (100, 425, 500, 100))
     #pygame.draw.rect (screen, SGRAY (100, 600, 500, 100))
     if i == 0:
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 75)
          screen.blit(noSave, noSavrect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 150)
          screen.blit(noSave, noSavrect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 225)
          screen.blit(noSave, noSavrect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 300)
          screen.blit(noSave, noSavrect)

          pygame.display.update()
     elif i == 1:
          
          saveOne = fontObj.render(temp[0], True, Image_dir.BLACK)
          saveOnerect = saveOne.get_rect()
          saveOnerect.center = (175, 125)
          screen.blit(saveOne, saveOnerect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 300)
          screen.blit(noSave, noSavrect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 450)
          screen.blit(noSave, noSavrect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 625)
          screen.blit(noSave, noSavrect)
          pygame.display.update()

     elif i == 2:
          t = temp[0][6:len(temp[0])-4]
          saveOne = fontObj.render(t, True, Image_dir.BLACK)
          saveOnerect = saveOne.get_rect()
          saveOnerect.center = (175, 125)
          screen.blit(saveOne, saveOnerect)

          t = temp[1][6:len(temp[1])-4]
          saveTwo = fontObj.render(t, True, Image_dir.BLACK)
          saveTworect = saveTwo.get_rect()
          saveTworect.center = (175, 300)
          screen.blit(saveTwo, saveTworect)

          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 450)
          screen.blit(noSave, noSavrect)
          
          noSavrect = noSave.get_rect()
          noSavrect.center = (175, 625)
          screen.blit(noSave, noSavrect)
          pygame.display.update()

     while True:
          for event in pygame.event.get():
               if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                         return
          
          








