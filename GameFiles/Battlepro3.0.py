from random import randrange

# list properties:
# Health, Mana, Stamina, Defense, Dodfe, Speed, Crit, Meldam, Rangedam, Magicdam
# Weakness, Elemental weakness, attack type, attack element, target, image

battle = [100,0,0,5,20,6,25,6,6,5,1,"f",0,"n",0,0,0]
abattle = [100,0,0,5,20,5,25,6,6,5,1,"a",0,"n",0,0,0]
aabattle = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
aaabattle = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

ebattle = [50,0,0,1,15,7,20,5,5,5,1,"if",0,"a",0,0,0]
eebattle = [50,0,0,1,15,4,20,5,5,5,0,"if",0,"n",0,0,0]
eeebattle = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
eeeebattle = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

i = 0

def enemyAttack(E):
    
    while True:
        target = randrange(0 , 40);
        print target
        attackType = randrange(0 , 1);
        print attackType
        E[12] = attackType

        if attackType < 2: #If the attack isn't a healing skill.
            if target <= 10 and battle[0]>0:
                E[14] = battle
                break
            elif target > 10 and target <=20 and abattle[0]>0:
                E[14] = abattle
                break
            elif target > 20 and target <=30 and aabattle[0]>0:
                E[14] = aabattle
                break
            elif target > 30 and target <=40 and aaabattle[0]>0:
                E[14] = aaabattle
                break

        elif attackType >2: #if the attack is a healing skill.
            if target <= 10 and target > 0 and ebattle[0]<80:
                E[14] = ebattle
                break
            elif target > 10 and target <=20 and eebattle[0]>0 and eebattle[0]<80:
                E[14] = eebattle
                break
            elif target > 20 and target <=30 and eeebattle[0]>0 and eeebattle[0]<80:
                E[14] = eeebattle
                break
            elif target > 30 and target <=40 and eeeebattle[0]>0 and eeeebattle[0]<80:
                E[14] = eeeebattle
                break


# Sorts based on speed with the highest first.
fightOrder = sorted([battle, ebattle, eebattle, eeebattle, eeeebattle, abattle, aabattle, aaabattle], key = lambda x: x[5], reverse=True)


while True:
    z = randrange(1, 100);
    h = randrange(1, 100);
    if ebattle[0] > 0 or eebattle[0] > 0 or eeebattle[0] > 0 or eeeebattle[0] > 0:

        if battle[0] <= 0:
            print "You have died.."
            break

        if battle[0] > 0:

            print "Use which attack?"
            battle[12] = int(raw_input())

            print "attack which enemy?"
            battle[14] = raw_input()
            if battle[14] == "0":
                battle[14] = ebattle
            elif battle[14] == "1":
                battle[14] = eebattle
            elif battle[14] == "2":
                battle[14] = eeebattle
            elif battle[14] == "3":
                battle[14] = eeeebattle

            elif battle[14] == "4":
                battle[14] = battle
            elif battle[14] == "5":
                battle[14] = abattle
            elif battle[14] == "6":
                battle[14] = aabattle
            elif battle[14] == "7":
                battle[14] = aaabattle

        if abattle[0] >0:

            print "Friend, use which attack?"
            abattle[12] = int(raw_input())

            print "Friend, attack which enemy?"
            abattle[14] = raw_input();
            if abattle[14] == "0":
                abattle[14] = ebattle
            elif abattle[14] == "1":
                abattle[14] = eebattle
            elif abattle[14] == "2":
                abattle[14] = eeebattle
            elif abattle[14] == "3":
                abattle[14] = eeeebattle

            elif abattle[14] == "4":
                abattle[14] = battle
            elif abattle[14] == "5":
                abattle[14] = abattle
            elif abattle[14] == "6":
                abattle[14] = aabattle
            elif abattle[14] == "7":
                abattle[14] = aaabattle

        if aabattle[0] >0:

            print "Friend, use which attack?"
            aabattle[12] = int(raw_input())

            print "Friend, attack which enemy?"
            aabattle[14] = raw_input();
            if aabattle[14] == "0":
                aabattle[14] = ebattle
            elif aabattle[14] == "1":
                aabattle[14] = eebattle
            elif aabattle[14] == "2":
                aabattle[14] = eeebattle
            elif aabattle[14] == "3":
                aabattle[14] = eeeebattle

            elif aabattle[14] == "4":
                aabattle[14] = battle
            elif aabattle[14] == "5":
                aabattle[14] = abattle
            elif aabattle[14] == "6":
                aabattle[14] = aabattle
            elif aabattle[14] == "7":
                aabattle[14] = aaabattle

        if aaabattle[0] >0:

            print "Friend, use which attack?"
            aaabattle[12] = int(raw_input())

            print "Friend, attack which enemy?"
            if aaabattle[14] == "0":
                aaabattle[14] = ebattle
            elif aaabattle[14] == "1":
                aaabattle[14] = eebattle
            elif aaabattle[14] == "2":
                aaabattle[14] = eeebattle
            elif aaabattle[14] == "3":
                aaabattle[14] = eeeebattle

            elif aaabattle[14] == "4":
                aaabattle[14] = battle
            elif aaabattle[14] == "5":
                aaabattle[14] = abattle
            elif aaabattle[14] == "6":
                aaabattle[14] = aabattle
            elif aaabattle[14] == "7":
                aaabattle[14] = aaabattle

        if ebattle[0]>0:
            print "Yep"
            enemyAttack(ebattle)
            
        if eebattle[0]>0:
            print "that's two"
            enemyAttack(eebattle)
            
        if eeebattle[0]>0:
            print "Three"
            enemyAttack(eeebattle)

        if eeeebattle[0]>0:
            print "Four"
            enemyAttack(eeeebattle)
            
        print "Almost in the for"
        for i in range(len(fightOrder)):
            if fightOrder[i][0]>0:
                if fightOrder[i][14][4] > h:
                    print "Dodged!"
                else:
                    print "Getting something. Maybe"
                    if fightOrder[i][12] == fightOrder[i][14][10] or str(fightOrder[i][13]) in str(fightOrder[i][14][11]):
                        if fightOrder[i][6] >= z:
                            print "Weakness + crit!"
                            if fightOrder[i][15] == 0: #melee attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][7]/fightOrder[i][14][3]) * 6)
                            elif fightOrder[i][15] == 1: #magic attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][9]/fightOrder[i][14][3]) * 6)
                            elif fightOrder[i][15] == 2: #range attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][8]/fightOrder[i][14][3]) * 6)
                        else:
                            print "Weakness"
                            if fightOrder[i][15] == 0: #melee attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][7]/fightOrder[i][14][3]) * 2)
                            elif fightOrder[i][15] == 1: #magic attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][9]/fightOrder[i][14][3]) * 2)
                            elif fightOrder[i][15] == 2: #range attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][8]/fightOrder[i][14][3]) * 2)

                    else:
                        if fightOrder[i][6] >= z:
                            print "Crit!"
                            if fightOrder[i][15] == 0: #melee attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][7]/fightOrder[i][14][3]) * 3)
                            elif fightOrder[i][15] == 1: #magic attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][9]/fightOrder[i][14][3]) * 3)
                            elif fightOrder[i][15] == 2: #range attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - ((fightOrder[i][8]/fightOrder[i][14][3]) * 3)
                        else:
                            if fightOrder[i][15] == 0: #melee attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - (fightOrder[i][7]/fightOrder[i][14][3])
                            elif fightOrder[i][15] == 1: #magic attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - (fightOrder[i][9]/fightOrder[i][14][3])
                            elif fightOrder[i][15] == 2: #range attack.
                                fightOrder[i][14][0] = fightOrder[i][14][0] - (fightOrder[i][8]/fightOrder[i][14][3])

    else:
        print "you win"
        break
    print battle[0]
    print abattle[0]
    print ebattle[0]
    print eebattle[0]


