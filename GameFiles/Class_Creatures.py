class character ():
    def __init__(self, name, magic, agility, strength, smarts, endurance, stamina, defense, description):
        self.name = name
        self.magic = magic
        self.agility = agility
        self.strength = strength
        self.smarts = smarts
        self.endurance = endurance
        self.stamina = stamina
        self.defense = defense
        self.description = description
    def __str__ (self):
        print (self.name)
        print ("Magic %d" % self.magic)
        print ("Agility %d" % self.agility)
        print ("Strength %d" % self.strength)
        print ("Smarts %d" % self.smarts)
        print ("Endurance %d" % self.endurance)
        print ("Stamina %d" % self.stamina)
        print ("Description")
        return (self.description)

"""Classes to choose from, if human character."""
Priest = character ("Priest", 6, 5, 4, 6, 6, 7, 30, "The art of healing and cursing has been woven into you. Yet, you're still ready to use the blunt end of your staff should the need arise. Weapons are; staff and magic.")
Warrior = character ("Warrior", 0, 5, 8, 5, 7, 8, 60, "Blood, you have studied long and hard on how to spill it from your opponents. Nevertheless, you're still a fair throw with a small axe. Weapons are; sword and throwing axe.")
Hunter = character ("Hunter", 3, 8, 4, 5, 7, 7, 45, "Tracking down and hunting your prey is second nature to you. Weapons are; bow and arrow, and knife.")
Thief = character ("Thief", 4, 8, 4, 6, 6, 7, 45, "Slipping around in the shadows have taught you how to move without being seen, until you want too. Weapons are; daggers and throwning knives.")
Scholar = character ("Scholar", 8, 4, 3, 8, 5, 4, 30, "Books have taught you a great many things, and you know what to use and where. weapons are; magic and wards.")
"""Elven Classes"""
Woodsman = character ("Woodsman", 3, 6, 7, 5, 7, 7, 40, "Leaping from branch to branch and moving through the forest is second nature to you. More than that is your powers with a bow, your shots rarely miss. Weapons are; Bow and arrow, and knife.")
Magicweaver = character ("Magicweaver", 9, 4, 3, 8, 6, 5, 50, "Long days and nights you've studied and practiced your magic and your control over it's enegry. Weapons are; staff and magic.")
Lightseeker = character ("Lightseeker", 7, 5, 4, 6, 6, 5, 50, "The powers of light flows through you and extends into your magic. You use the guiding light of the gods/goddess of nature for your magic and your life. Weapons are; magic and wards.")
Darkseeker = character ("Darkseeker", 8, 6, 3, 7, 6, 6, 40, "Darkness swirls around your fingers allowing you to bend the light around you, which makes your strike all the more deadlier. Weapons are; daggers and magic.")
Vitacere = character ("Vitacere", 9, 5, 3, 7, 5, 5, 30, "Magic is a talent of yours, but you've choosen a different path than most. Using your magic to understand animals, and life more. Magic is the center of this class, you use magic and attempt to sway creatures rather than attack. Weapons are; magic.")


class beasts ():
    def __init__(self, name, image, magic, agility, strength, smarts, endurance, stamina, defense, attack_chance, att_power):
        self.name = name
        self.image = image
        self.magic = magic
        self.agility = agility
        self.strength = strength
        self.smarts = smarts
        self.endurance = endurance
		self.stamina = stamina
        self.defense = defense
		self.attack_chance = attack_chance
		self.att_power = att_power
		
	
class humanoid ():
    def __init__(self, name, image, magic, agility, strength, smarts, endurance, stamina, weapon, defense, attack_chance, att_1, att_2):
        self.name = name
        self.image = image
        self.magic = magic
        self.agility = agility
        self.strength = strength
        self.smarts = smarts
        self.endurance = endurance
        self.stamina = stamina
        self.weapon = weapon
		self.defense = defense
		self.attack_chance = attack_chance
		self.att_1 = att_1
		self.att_2 = att_2
		
"""Tutorial emeny"""
Tute = humanoid ("First fight", 'image', 4, 5, 5, 5, 5, 5, shortisw, 30, 50, stab, slash)