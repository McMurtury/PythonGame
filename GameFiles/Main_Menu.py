import pygame, sys, Image_dir
from pygame.locals import *
from Image_dir import *

pygame.init()

mouse_x = 0
mouse_y = 0

screen = pygame.display.set_mode((800, 600))
corner1 = (400, 200)
corner2 = (475)
corner3 = (550) 
corner4 = (625) 
corner5 = (700)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
SGRAY =  (49,79, 79)

def mainmenu():
		while True:
				m = 0
				screen.fill((WHITE))
				screen.blit (Image_dir.ng, (300, 200))
				screen.blit (Image_dir.cg, (300, 275))
				screen.blit (Image_dir.om, (300, 350))
				screen.blit (Image_dir.cd, (300, 425))
				screen.blit (Image_dir.qt, (300, 500))
				pygame.display.update()
				for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            break
                                        




