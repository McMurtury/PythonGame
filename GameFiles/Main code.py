import pygame, sys, Image_dir
from pygame.locals import *
from Image_dir import *
from classes_selec import *
from Race_name import *
from Main_Menu import *


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Testing')

player_char = ['Name', 'Race', 'Gender', 'Class', 'Char Image','Gold amount','Hp','Mp','armor','weapon1','weapon2','arrows', 'combat multipler']
player_charatt = ['Attack 1', 'Attack 2', 'Attack 3', 'Attack 4']


race (player_char)
gender (player_char)
if player_char[1].lower() == 'human':
    classh(player_char)
elif player_char[1].lower() == 'elf':
    classe(player_char)
name (player_char)
player_char[4] = Image_dir.stickman
screen.fill((WHITE))
screen.blit (player_char[4], (400, 300))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
