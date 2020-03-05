import pygame, sys, Image_dir, Class_list

#items

heatlhP = Class_list.item ("Health Potion", pygame.image.load('health_potionM.png'), pygame.image.load('health_potion.png'), 0, 0, "Restores 20% health upon use.", 3000)
staminaP = Class_list.item ("Stamina Potion", pygame.image.load('stamina_potionM.png'), pygame.image.load('stamina_potion.png'), 0, 1, "Restores 20% stamina upon use.", 100)
manaP = Class_list.item ("Mana Potion", pygame.image.load('mana_potionM.png'), pygame.image.load('mana_potion.png'), 0, 2, "Restores 20% mana upon use.", 100)



#weapons
