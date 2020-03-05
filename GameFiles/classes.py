class character ():
	def __init__(self, name, magic, agility, strength, smarts, endurance, stamina, background):
		self.name = name
		self.magic = magic
		self.agility = agility
		self.strength = strength
		self.smarts = smarts
		self.endurance = endurance
		self.stamina = stamina
		self.background = background
	def description (self):
		print (self.name)
		print ("Magic %d" % self.magic)
		print ("Agility %d" % self.agility)
		print ("Strength %d" % self.strength)
		print ("Smarts %d" % self.smarts)
		print ("Endurance %d" % self.endurance)
		print ("Stamina %d" % self.stamina)
		print ("Background")
		print (self.background)

"""Classes to choose from, if human character."""
Preist = character ("Preist", 6, 5, 4, 6, 6, 7, "Studing the ways of the gods have taught you many secrets. Yet you feel your wisedom lacking in some areas, which is why you move from the temple and seek out the mysteries of the world.")
Warrior = character ("Warrior", 0, 5, 8, 5, 7, 8, "War is what you know best. From early childhood you have been training with your weapon and seeking to best your master. Yet, you feel a desire to roam around the world. To see and experince life, and not just take it.")
Hunter = character ("Hunter", 3, 7, 4, 5, 7, 7, "Your father taught you how to live off the land, and you've made full use of the skills you learned. Yet you feel the need to seek out other people for interactioins rather than living completely alone with nature.")
Thief = character ("Thief", 4, 8, 4, 6, 6, 7, "Thrown into a dark alley from the day of your birth, you learned quickly the ways of the street. Along with a very simple lesson. It isn't pretty or glamorous, but it is my life and I will survive.")
Scholar = character ("Scholar", 7, 4, 3, 8, 5, 4, "Books and knowledge is your life. Learning the sercets of the past and pushing forward with the study of magic for the good of the empire. The endless cycle of studying and training your magic is all you've ever known.")
"""Elven Classes"""
Woodsman = character ("Woodsman", 3, 6, 7, 5, 7, 7, "BS")
Lightseeker = character ("Lightseeker", 7, 5, 4, 6, 6, 5 "BS")
Magicweaver = character ("Magicweaver", 9, 4, 4, 8, 6, 5, "BS")
Darkseeker = character ("Darkseeker", 8, 6, 3, 7, 6, 6, "bS")

race = raw_input ("Human, elf, or something else?"):
if race.lower() == "human":
	return race == 0:
	print ("Choose your class.")
	Preist.description
	Warrior.description
	Hunter.description
	Thief.description
	Scholar.description
	char = raw_input ("Type the first letter of the class you choose."):
		if char.lower() == "p":
			return char == 0
		elif char.lower() == "w"
			return char == 1
		elif char.lower() == "h"
			return char == 2
		elif char.lower() == "t"
			return char == 3
		elif char.lower() == "s"
			return char == 4

elif race.lower() == "elf":
	return race == 1

else print ("You can not be that....yet.")

print ("Choose your class.")
print ("1 for Preist.")
print ("2 for Warrior.")
print ("3 for Hunter.")
print ("4 for Thief.")
print ("5 for Scholar.")


if playerchar == 1:
	Preist.description()
elif playerchar == 2:
	Warrior.description()
elif playerchar == 3:
	Hunter.description()

Thief.description()
Scholar.description()
raw_input()


