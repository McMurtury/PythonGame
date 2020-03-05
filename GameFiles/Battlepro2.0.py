import math
from random import randrange

player_char = ['agility','strength','weapondamage',50,0]

player_char[0] = 5
player_char[1] = 4
player_char[2] = 8
player_char[4] = 5

emeny = ['agility','strength','weapondamage',30,0]

emeny[0] = 7
emeny[1] = 5
emeny[2] = 5
emeny[4] = 7


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
def speed(S):
        S[5] = (m*ss*2.5)/10

battle = [0,0,0,0,100,0,0]
abattle = [9,30,7,7, 100,7,0]
aabattle = [0,0,0,0, 100,0,0]
aaabattle = [0,0,0,0, 100,0]

ebattle = [0,0,0,0,50,0,0]
eebattle = [9,35,5,7, 50,4,0]
eeebattle = [0,0,0,0, 0,0,0]
eeeebattle = [0,0,0,0, 0,0,0]

n = emeny[0]
m = player_char[0]
0s = player_char[1]
w = player_char[2]
ss = player_char[4]
d = emeny [3]
meldam(battle)
crit(battle)
dodged(battle)
speed(battle)

n = player_char[0]
m = emeny[0]
s = emeny[1]
w = emeny[2]
ss = emeny[4]
d = player_char[3]
meldam(ebattle)
crit(ebattle)
dodged(ebattle)
speed(ebattle)

i = 0

ebattle[6] = battle
eebattle[6] = abattle

fightOrder = sorted([battle, ebattle, eebattle, eeebattle, eeeebattle, abattle, aabattle, aaabattle], key = lambda x: x[5], reverse=True)

while True:
    z = randrange(1, 100);
    h = randrange(1, 100);
    if ebattle[4] > 0 or eebattle[4] > 0 or eeebattle[4] > 0 or eeeebattle[4] > 0:
        
        if battle[4] ==0:
            print "You have died.."
            break
        print "attack enemy 1 or 2?"
        battle[6] = raw_input()
        if battle[6] == "1":
            battle[6] = ebattle
        if battle[6] == "2":
            battle[6] = eebattle
    
    
        if abattle[4] >0:
            print "Friend, attack enemy 1 or 2?"
            abattle[6] = raw_input();
            if abattle[6] == "1":
                abattle[6] = ebattle
            if abattle[6] == "2":
                abattle[6] = eebattle

        for i in range(len(fightOrder)):
                if fightOrder[i][4]>0:
                    if fightOrder[i][6][0] > h:
                        print "dodged"
                    else:
                        if fightOrder[i][1]>=z:
                            print "Crit"
                            fightOrder[i][6][4] = fightOrder[i][6][4] - (fightOrder[i][2]*3)
                        else:
                            fightOrder[i][6][4] = fightOrder[i][6][4] - fightOrder[i][2]
    

    else:
        print "You win"
        break
    print battle[4]
    print abattle[4]
    print ebattle[4]
    print eebattle[4]



