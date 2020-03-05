import math
"""
A = player_char[0]
s = player_char[3].strength
d = defense
m = player_char[3].magic
w = weapondam
sp = player_char[3].stamina
ep = player_char[3].endurance
so = enemy.stamina
eo = enemy.endurance
"""

#crit chance equ
def crit():
	x = 3.14*O*A*1.34
	y = 3.14159*(4*A - O)
	r = (x/(x-y))**4
	c = math.sqrt(r)


#dodge chance equ
def dodge(D):
	x = (emeny[0]+player_char[0])**2 * (4.957*player_char[0] - 3.1459*(emeny[0]/2))
	y = (1.39*emeny[0])*(emeny[0]-1.75*emeny[0]+3.4*player_char[0])
	r = math.sqrt(((x**3)/(2.67*x+y**2))**4)
	c = (r/((3.1459**2)*(emeny[0]+3*A)-5*emeny[0]))*.0374*(1/r)
	D[4] = (1/c)/(100*O)+.83*player_char[0]**1.5-emeny[0]

#melee damage equ
def meldam(Y):
	x = w*8*(s*2)
	Y[2] = (x+2*m)/d

#Range Damage equ
def randam():	
	x = w*8*(A*2)
	y = (x+2*s)/d

#Magic damage equ
def magdam():
	x = w*8*(m*3)
	y = (x+2*s)/(1.75*d)

#Escape chance
def escap():
	x = (f**2)+ (sp+so)*0.35-(eo-ep)**2
	y = x/((4*(sp-so)*ep)**2)
