import pygame, sys, Image_dir, Class_list, textwrap
from pygame.locals import *
from Image_dir import *

pygame.init()

mouse_x = 0
mouse_y = 0

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Main')


def gameStart():
    fontObj = pygame.font.Font(None, 30)
    screen.fill(Image_dir.SGRAY)
    
    with open ('Text\Intro.txt', 'r') as f:
         data = f.readlines()
         for line in data:
              temp = line
    test = textwrap.wrap(temp, 60)
    i = 0
    while True:
        
        text = fontObj.render(test[i], True, BLACK)
        screen.blit (text, (75, (75 + (i*25))))
        pygame.display.update()
        i = i + 1
        if i == (len(test)):
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

gameStart()
pygame.quit()
sys.exit()
