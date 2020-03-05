import pygame, sys, classes_selec
from pygame.locals import *

#color codes
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


#main menu buttons
ng = pygame.image.load('Images/ng.png')
cg = pygame.image.load('Images/cg.png')
om = pygame.image.load('Images/om.png')
cd = pygame.image.load('Images/cd.png')
qt = pygame.image.load('Images/quit.png')

#Gender selection
genderSelect = pygame.image.load('Images/genderSelect.png')
female = pygame.image.load('Images/Female.png')
male = pygame.image.load('Images/Male.png')

#Class selection
startingClass = pygame.image.load('Images/StartingClass.png')
chWarrior = pygame.image.load('Images/checkWarrior.png')
chThief = pygame.image.load('Images/checkThief.png')
chMage = pygame.image.load('Images/checkMage.png')

#Attribute selection
attribute = pygame.image.load('Images/attribute.png')
bar = pygame.image.load('Images/Bar.png')

#Yes/No images.
yesi = pygame.image.load('Images\yes.png')
noi = pygame.image.load('Images\cn.png')

#Character Confrims.
confrimMage = pygame.image.load('Images\confrimM.png')
confrimThief = pygame.image.load('Images\confrimT.png')
confrimWarrior = pygame.image.load('Images\confrimW.png')


#Battle effects images

#Stat images

#Map images

#Background images.
townStart = pygame.image.load('Images\HomeTown.png')

storyTell = pygame.image.load('Images\ElderStoryteller.png')
