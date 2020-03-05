import pygame, sys, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Map Test')

mp = pygame.image.load('mapS1.png')
pi = pygame.image.load('pi.png')


x = 527
y = 285
w = 0
player_pos = [x,y, 'city',w,0]

wmsi = [527255,542270,542285,527315,512330,512345,512360,512375,512390,512405,512420,512435,497450,497465,482480,497480,467480,467495,452495,437495,422495,422510,422525,392525,392540,392555,37755,362555,362570,347570,332570,332585,317585,302585,287585,272585,257585,242585,227585,212585,212570,197570,182570,182555,167555,152555,137555,122555,107555,92555,77555,62555,62540,47540,47525,32525,17525,17510,17495,17480,17465,32465,17450,17435,17420,32420,32405,47405,62405,62390,77390,92390,107390,122390,122375,122360,137360,137345,137330,122330,122315,122300,122285,137285,137270,152270,167270,167255,182255,167240,167225,167210,182210,182192,182180,197180,197165,197150,197135,197120,212120,212105,182120,182105,167105,16790,15290,13790,12290,10790,107105,107120,92120,92135,77135,62135,62150,62165,62180,62195,47195,47210,32210,542255,527290,527225,527210,527195,512195,497195,497180,497165,482165,482150,467150,452150,437150,437165,437180,437195,422195,422210,422225,422240,437240,437255,437270,437285,422285,422300,422315,422330,422345,422360,407360,407375,392375,377375,377360,377345,377330,377312,377300,377285,377270,377255,377240,377225,377210,377195,392195,392180,407180,407165,407150,407135,422135,437135,437120,452120,467120,467105,482120,497120,512120,512135,527135,452135,36230,34730,33230,31730,30230,542300,377195,392195,542135,182195,197195,542315,527330,512450,407525,377555,92555,77555,527240,407375,407360,377315]
rmsi = [512300,497315,482330,467345,452345,437360,422375,437375,422390,407405,392405,392390,377405,377390,362390,362375,347375,332375,332390,317390,317405,302405,302390,287390,287405,512270,497255,512255,512240,497240,497225,497210,482210,482195,257420,242420,257435,242435,242450,257450,227465,227450,212465,212450,197465,182480,167495,152510,137525,137510,122510,122525,107510,92495,92510,77495,77510,62510,62495,47495,47510,32494,32480,47480,47465,47450,62435,47435,77420,92420,107420,122420,122405,137405,152405,152390,137390,137375,152375,212405,197390,197405,182390,167375,152360,152345,167345,167330,182315,182300,197285,212270,197270,197255,212255,227255,227240,242240,242225,257225,272210,287195,287180,302180,287165,287150,272135,287135,257120,242120,242105,227105,347345,332345,332330,317315,332315,317300,302300,302285,287285,272285,272300,257315,272315,257330,257345,257360,257375,287270,287255,287240,302240,302225,302210,302195,317195,332195,347195,362195,362180,347180]
def chc (C):
        if 428 <= player_pos[0] <= 456 and 350 <= player_pos[1] <= 379:
                print 'enter city 1'
                player_pos[2]= 'city1'
                return True
        elif 475 <= player_pos[0] <= 492 and 184 <= player_pos[1] <= 201:
                print 'enter city 2'
                player_pos[2] = 'city2'
                return True
        elif 349 <= player_pos[0] <= 374 and 349 <= player_pos[1] <= 381:
                print 'enter city 3'
                player_pos[2] = 'city3'
                return True
        elif 222 <= player_pos[0] <= 291 and 387 <= player_pos[1] <= 434:
                print 'enter city cap'
                player_pos[2] = 'cap'
                return True
        elif 31 <= player_pos[0] <= 54 and 501 <= player_pos[1] <= 525:
                print 'enter city 4'
                player_pos[2] = 'city4'
                return True
        elif 63 <= player_pos[0] <= 85 and 419 <= player_pos[1] <= 441:
                print 'enter city 5'
                player_pos[2] = 'city5'
                return True
        elif 142 <= player_pos[0] <= 169 and 357 <= player_pos[1] <= 391:
                print 'enter city costal'
                player_pos[2] = 'costal'
                return True
        elif 192 <= player_pos[0] <= 219 and 244 <= player_pos[1] <= 274:
                print 'enter city 6'
                player_pos[2] = 'city6'
                return True
        elif 288 <= player_pos[0] <= 321 and 191 <= player_pos[1] <= 220:
                print 'enter city 7'
                player_pos[2] = 'city7'
                return True
        elif 365 <= player_pos[0] <= 391 and 177 <= player_pos[1] <= 202:
                print 'enter city 8'
                player_pos[2] = 'city8'
                return True
        elif 526 <= player_pos[0] <= 546 and 281 <= player_pos[1] <= 307:
                print 'enter city 9'
                player_pos[2] = 'city9'
                return True
        
                
                
def mov (M):
        while True:
            if player_pos[4] == 110:
                    if chc(player_pos) == True:
                            break
            elif player_pos[4]>10:
                    player_pos[4] = 0
                    break
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.key == K_d:
                        M[0] = M[0]+15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[0] = M[0]-15
                                                
                    elif evt.key == K_w:
                        M[1] = M[1]-15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[1] = M[1]+15
                                             
                    elif evt.key == K_s:
                        M[1] = M[1]+15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[1] = M[1]-15
                        
                    elif evt.key == K_a:
                        M[0] = M[0]-15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[0] = M[0]+15
                                                
                    elif evt.key == K_e:
                        M[0] = M[0]+15
                        M[1] = M[1]-15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[0] = M[0]-15
                                M[1] = M[1]+15
                                                
                    elif evt.key == K_q:
                        M[0] = M[0]-15
                        M[1] = M[1]-15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[0] = M[0]+15
                                M[1] = M[1]+15
                                               
                    elif evt.key == K_z:
                        M[0] = M[0]-15
                        M[1] = M[1]+15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[0] = M[0]+15
                                M[1] = M[1]-15
                                                
                    elif evt.key == K_c:
                        M[0] = M[0]+15
                        M[1] = M[1]+15
                        player_pos[3] = int(str(player_pos[0]) + str(player_pos[1]))
                        if player_pos[3] not in wmsi:
                                screen.blit (mp, (0,0))
                                screen.blit (pi, (player_pos[0],player_pos[1]))
                                pygame.display.update()
                                player_pos[4]=1+player_pos[4]
                                if player_pos[3] not in rmsi:
                                        player_pos[4]= 1+player_pos[4]
                                else:
                                        print "road"
                                print player_pos[3]
                        else:
                                M[0] = M[0]-15
                                M[1] = M[1]-15
                        

screen.blit (mp, (0,0))
screen.blit (pi, (player_pos[0],player_pos[1]))
pygame.display.update()
mov (player_pos)
screen.blit (pi, (player_pos[0],player_pos[1]))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
