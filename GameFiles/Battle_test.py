import pygame, sys, classes_selec, Image_dir
from pygame.locals import *
from Image_dir import *
from Equations import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Testing')
critc = 0
dodc = 0
meld = 0
rand = 0


mouse_x = 0
mouse_y = 0

corner1 = (50, 350)
corner2 = (300)
corner3 = (550)
corner4 = (175, 475)
corner5 = (425)


screen.fill((WHITE))
screen.blit (Image_dir.mel, (50, 350))
screen.blit (Image_dir.defe, (300, 350))
screen.blit (Image_dir.rang, (550, 350))
screen.blit (Image_dir.mag, (175, 475))
screen.blit (Image_dir.run, (425, 475))
pygame.display.update()

def bat_start:
    critc = crit(player_char)
    dodc = dodge(player_char)
    meld = meldam(player_char)
    rand = randam(player_char) 
    esc = escap(player_char)
    magd = magdam(player_char)


while True:
    for event in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                mouse_x, mouse_y = event.pos
                                                if mouse_x >= corner1 [0] and mouse_x <= corner1[0]+200 and mouse_y >= corner1 [1] and mouse_y <= corner1 [1]+100:
                                                    screen.fill ((SGRAY))
                                                    pygame.display.update()
														
				

				
				
				
				
				
				
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
