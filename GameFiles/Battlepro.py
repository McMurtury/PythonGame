import math
from random import randrange

player_char = ['agility','strength','weapondamage',50,0]

player_char[0] = 5
player_char[1] = 5
player_char[2] = 5

emeny = ['agility','strength','weapondamage',50,0]

emeny[0] = 6
emeny[1] = 5
emeny[2] = 5

def dodged(D):
        x = (n+m)**2 * (4.957*m - 3.1459*(n/2))
        y = (1.39*n)*(n-1.75*n+3.4*m)
        r = math.sqrt(((x**3)/(2.67*x+y**2))**4)
        c = (r/((3.1459**2)*(n+3*m)-5*n))*.0374*(1/r)
        D[0] = (1/c)/(100*n)+.83*m**1.5-n
def crit(C):
        x = 3.14*n*m*1.34
        y = 3.14159*(4*m - n)
        r = (x+y)*m
        if r > 0:
                C[1] = math.sqrt(r)+m
        else:
                C[1] = m
def meldam(Y):
	x = w*8*(s*2)
	Y[2] = (x+2*m)/d
        
battle = [0,0,0,0]
ebattle = [0,0,0,0]

n = emeny[0]
m = player_char[0]
s = player_char[1]
w = player_char[2]
d = emeny [3]
meldam(battle)
crit(battle)
dodged(battle)

n = player_char[0]
m = emeny[0]
s = emeny[1]
w = emeny[2]
d = player_char[3]
meldam(ebattle)
crit(ebattle)
dodged(ebattle)


z = randrange(1, 100);
h = randrange(1, 100);
if battle[1] >= z:
        battle[3] = 1
else:
        battle[3] = 0

if ebattle[1] >= z:
        ebattle[3] = 1
else:
        ebattle[3] = 0

print z
print h
print "player"
print battle[1]
print battle[2]
print battle[0]
if battle[3] == 1:
        print battle[2]*3
if battle[0] >= h:
        print "Dodged"
else:
        print "You didn't dodge"

print "Enemy"
print ebattle[1]
print ebattle[2]
print ebattle[0]
if ebattle[3] == 1:
        print ebattle[2]*3
if ebattle[0] >= h:
        print "he dodged"
else:
        print "he didn't dodge."
"""print z
if battle[2] >= z:
        print "You hit crit"
else:
        print "no crit"

if ebattle[1] >= z:
        print "You hit crit"
else:
        print "no crit"
print battle[1]
print ebattle[1]

if battle[0] >= z:
        print "Dodged"
else:
        print "no good."
if ebattle[0] >= z:
        print "he dodged"
else:
        print "he didn't dodge."

print battle[0]
print ebattle[0]"""


