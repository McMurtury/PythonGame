import pygame, sys, classes_selec, Image_dir
from pygame.locals import *
from Image_dir import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Testing')

mouse_x = 0
mouse_y = 0


corner1 = (150, 150)
corner2 = (350, 300)
corner3 = (550, 450)
corner4 = (700, 450)

WHITE = (255, 255, 255)
SGRAY = (49, 79, 79)

fontObj = pygame.font.Font('FFF_Tusj-webfont.ttf', 60)
textSurfaceObj = fontObj.render('What is your class?', True, SGRAY)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400, 75)
check = fontObj.render('Are you sure?', True, SGRAY)
checkrect = check.get_rect()
checkrect.center = (425, 25)




def classh(C):
        while True:
                x = 0
                y = 0
                screen.fill((WHITE))
                screen.blit (textSurfaceObj, textRectObj)
                screen.blit (Image_dir.wi, (150, 150))
                screen.blit (Image_dir.ti, (150, 300))
                screen.blit (Image_dir.si, (350, 450))
                screen.blit (Image_dir.hi, (550, 150))
                screen.blit (Image_dir.pi, (550, 300))
                pygame.display.update()
                if x == 0:
                        for event in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                mouse_x, mouse_y = event.pos
                                                if mouse_x >= corner1 [0] and mouse_x <= corner1[0]+100 and mouse_y >= corner1 [1] and mouse_y <= corner1 [1]+100:
                                                    while y == 0:
                                                        screen.fill((WHITE))
                                                        screen.blit(Image_dir.wd, (225, 75))
                                                        screen.blit(check, checkrect)
                                                        screen.blit(Image_dir.yesi, (700, 450))
                                                        screen.blit(Image_dir.noi, (700, 550))
                                                        pygame.display.update ()
                                                        for event in pygame.event.get():
                                                            if event.type == MOUSEBUTTONDOWN:
                                                                    if event.button == 1:
                                                                                mouse_x, mouse_y = event.pos
                                                                                if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                        C[3] = 1
                                                                                        x = 1
                                                                                        return
                                                                                elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                        y = 1
                                                                                        
                                        
                                                elif mouse_x >= corner1 [0] and mouse_x <= corner1[0]+100 and mouse_y >= corner2 [1] and mouse_y <= corner2 [1]+100:
                                                    while y == 0:
                                                        screen.fill((WHITE))
                                                        screen.blit(Image_dir.td, (225, 75))
                                                        screen.blit(check, checkrect)
                                                        screen.blit(Image_dir.yesi, (700, 450))
                                                        screen.blit(Image_dir.noi, (700, 550))
                                                        pygame.display.update ()
                                                        for event in pygame.event.get():
                                                            if event.type == MOUSEBUTTONDOWN:
                                                                    if event.button == 1:
                                                                                mouse_x, mouse_y = event.pos
                                                                                if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                        C[3] = 2
                                                                                        x = 1
                                                                                        return
                                                                                elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                        y = 1
                                                                                
                                                elif mouse_x >= corner1 [0]+200 and mouse_x <= corner1[0]+300 and mouse_y >= corner3 [1] and mouse_y <= corner3 [1]+100:
                                                    while y == 0:
                                                        screen.fill((WHITE))
                                                        screen.blit(Image_dir.sd, (225, 75))
                                                        screen.blit(check, checkrect)
                                                        screen.blit(Image_dir.yesi, (700, 450))
                                                        screen.blit(Image_dir.noi, (700, 550))
                                                        pygame.display.update ()
                                                        for event in pygame.event.get():
                                                            if event.type == MOUSEBUTTONDOWN:
                                                                    if event.button == 1:
                                                                                mouse_x, mouse_y = event.pos
                                                                                if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                        C[3] = 3
                                                                                        x = 1
                                                                                        return
                                                                                elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                        y = 1
                                                                                        
                                                elif mouse_x >= corner3 [0] and mouse_x <= corner3[0]+100 and mouse_y >= corner1 [1] and mouse_y <= corner1 [1]+100:
                                                    while y == 0:
                                                        screen.fill((WHITE))
                                                        screen.blit(Image_dir.hd, (225, 75))
                                                        screen.blit(check, checkrect)
                                                        screen.blit(Image_dir.yesi, (700, 450))
                                                        screen.blit(Image_dir.noi, (700, 550))
                                                        pygame.display.update ()
                                                        for event in pygame.event.get():
                                                            if event.type == MOUSEBUTTONDOWN:
                                                                    if event.button == 1:
                                                                                mouse_x, mouse_y = event.pos
                                                                                if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                        C[3] = 4
                                                                                        x = 1
                                                                                        return
                                                                                elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                        y = 1
                                                                                
                                                                    
                                                                                        
                                                elif mouse_x >= corner3 [0] and mouse_x <= corner3[0]+100 and mouse_y >= corner2 [1] and mouse_y <= corner2 [1]+100:
                                                    while y == 0:
                                                        screen.fill((WHITE))
                                                        screen.blit(Image_dir.pd, (225, 75))
                                                        screen.blit(check, checkrect)
                                                        screen.blit(Image_dir.yesi, (700, 450))
                                                        screen.blit(Image_dir.noi, (700, 550))
                                                        pygame.display.update ()
                                                        for event in pygame.event.get():
                                                            if event.type == MOUSEBUTTONDOWN:
                                                                    if event.button == 1:
                                                                                mouse_x, mouse_y = event.pos
                                                                                if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                        C[3] = 5
                                                                                        x = 1
                                                                                        return
                                                                                elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                        y = 1
                elif x == 1:
                        break
def classe(C):
        while True:
            x = 0
            y = 0
            screen.fill((WHITE))
            screen.blit (textSurfaceObj, textRectObj)
            screen.blit (Image_dir.wi, (150, 150))
            screen.blit (Image_dir.mi, (150, 300))
            screen.blit (Image_dir.vi, (350, 450))
            screen.blit (Image_dir.di, (550, 150))
            screen.blit (Image_dir.li, (550, 300))
            pygame.display.update()
            if x == 0:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                mouse_x, mouse_y = event.pos
                                                if mouse_x >= corner1 [0] and mouse_x <= corner1[0]+100 and mouse_y >= corner1 [1] and mouse_y <= corner1 [1]+100:
                                                        while y == 0:
                                                                screen.fill((WHITE))
                                                                screen.blit(Image_dir.dw, (225, 75))
                                                                screen.blit(check, checkrect)
                                                                screen.blit(Image_dir.yesi, (700, 450))
                                                                screen.blit(Image_dir.noi, (700, 550))
                                                                pygame.display.update ()
                                                                for event in pygame.event.get():
                                                                    if event.type == MOUSEBUTTONDOWN:
                                                                            if event.button == 1:
                                                                                        mouse_x, mouse_y = event.pos
                                                                                        if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                                C[3] = 6
                                                                                                x = 1
                                                                                                return
                                                                                        elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                                y = 1
                                        
                                                elif mouse_x >= corner1 [0] and mouse_x <= corner1[0]+100 and mouse_y >= corner2 [1] and mouse_y <= corner2 [1]+100:
                                                        while y == 0:
                                                                screen.fill((WHITE))
                                                                screen.blit(Image_dir.md, (225, 75))
                                                                screen.blit(check, checkrect)
                                                                screen.blit(Image_dir.yesi, (700, 450))
                                                                screen.blit(Image_dir.noi, (700, 550))
                                                                pygame.display.update ()
                                                                for event in pygame.event.get():
                                                                    if event.type == MOUSEBUTTONDOWN:
                                                                            if event.button == 1:
                                                                                        mouse_x, mouse_y = event.pos
                                                                                        if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                                C[3] = 7
                                                                                                x = 1
                                                                                                return
                                                                                        elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                                y = 1
                                                                                
                                                elif mouse_x >= corner1 [0]+200 and mouse_x <= corner1[0]+300 and mouse_y >= corner3 [1] and mouse_y <= corner3 [1]+100:
                                                        while y == 0:
                                                                screen.fill((WHITE))
                                                                screen.blit(Image_dir.vd, (225, 75))
                                                                screen.blit(check, checkrect)
                                                                screen.blit(Image_dir.yesi, (700, 450))
                                                                screen.blit(Image_dir.noi, (700, 550))
                                                                pygame.display.update ()
                                                                for event in pygame.event.get():
                                                                    if event.type == MOUSEBUTTONDOWN:
                                                                            if event.button == 1:
                                                                                        mouse_x, mouse_y = event.pos
                                                                                        if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                                C[3] = 8
                                                                                                x = 1
                                                                                                return
                                                                                        elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                                y = 1
                                                elif mouse_x >= corner3 [0] and mouse_x <= corner3[0]+100 and mouse_y >= corner1 [1] and mouse_y <= corner1 [1]+100:
                                                        while y == 0:
                                                                screen.fill((WHITE))
                                                                screen.blit(Image_dir.dd, (225, 75))
                                                                screen.blit(check, checkrect)
                                                                screen.blit(Image_dir.yesi, (700, 450))
                                                                screen.blit(Image_dir.noi, (700, 550))
                                                                pygame.display.update ()
                                                                for event in pygame.event.get():
                                                                    if event.type == MOUSEBUTTONDOWN:
                                                                            if event.button == 1:
                                                                                        mouse_x, mouse_y = event.pos
                                                                                        if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                                C[3] = 9
                                                                                                x = 1
                                                                                                return
                                                                                        elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                                y = 1
                                                                                        
                                                elif mouse_x >= corner3 [0] and mouse_x <= corner3[0]+100 and mouse_y >= corner2 [1] and mouse_y <= corner2 [1]+100:
                                                        while y == 0:
                                                                screen.fill((WHITE))
                                                                screen.blit(Image_dir.ld, (225, 75))
                                                                screen.blit(check, checkrect)
                                                                screen.blit(Image_dir.yesi, (700, 450))
                                                                screen.blit(Image_dir.noi, (700, 550))
                                                                pygame.display.update ()
                                                                for event in pygame.event.get():
                                                                    if event.type == MOUSEBUTTONDOWN:
                                                                            if event.button == 1:
                                                                                        mouse_x, mouse_y = event.pos
                                                                                        if mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1] and mouse_y <= corner4[1]+50:
                                                                                                C[3] = 10
                                                                                                x = 1
                                                                                                return
                                                                                        elif mouse_x >= corner4[0] and mouse_x <= corner4[0]+100 and mouse_y >= corner4[1]+100 and mouse_y <= corner4[1]+150:
                                                                                                y = 1
            elif x == 1:
                    break




