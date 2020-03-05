class weapons ():
    def __init__(self, name, att_power, description, value):
        self.name = name
        self.att_power = att_power
        self.description = description
        self.value = value

class magic ():
    def __init__(self, name, att_power, description):
        self.name = name
        self.att_power = att_power
        self.description = description
        
class attack ():
     def __init__(self, name ,element , attType, archType, spCost, mpCost, image):
         self.name = name
         self.element
         self.attType
         self.archType
         self.spCost
         self.mpCost
         self.image

slash = attack ("Slash", "none", 0, 0, 5, 0, pygame.image.load('attack_One.png'))
		
#Swords
longisw = weapons ("Iron Long Sword", 18, "The most standard weapon in all the world.",)
longssw = weapons ("Steel Long Sword", 25, "The improved verison of the iron long sword. It's sharp and will keep it's edge through many uses.",)
32
45
shortisw = weapons ("Iron Short Sword", 12, "Shorter than a Long sword. But still sharp enough to cut.",)
shortssw = weapons ("Steel Short Sword", 19, "Stronger that iron, but still shorter than the long sword. Pointy end should always be pointed away from you.",)
26
33

#daggers
irondr = weapons ("Iron Dagger", 11, "Simple dagger made from a reliable material.",)
irondrc = weapons ("Cruved Iron Dagger", 13, "Simple iron dagger with a cruved blade.",)
sdr = weapons ("Steel Dagger", 16, "Stronger than it's iron counterpart, keeps a better edge as well.",)
sdrc = weapons ("Cruved Steel Dagger", 18, "Steel dagger with a cruved blade. Guaranteed to cut.",)
21
23
26
28

#Bows
wbow = weapons ("Wooden Bow", 10, "Simple bow handmade from wood. It is a trusted starter bow for most.",)
hwbow = weapons ("Hard Wood Bow", 14, "Hand craved from a hardwood tree, this is a soild bow that will rarely miss the mark.",)
dwbow = weapons ("Dark Wood Bow", 18, "Dark wood trees flex better than most woods, allowing for better speed on the arrow.",)
awbow = weapons ("Ancient Wood Bow", 25, "Wood of this caliber only comes from trees that are hunderds of years old.",)

#Arrows
wtarr = weapons ("Wooden Arrows", 3, "Thin pieces of wood with feathers attached to the end. They aren't the prettiest, but they will get the job done.",)
starr = weapons ("Stone Tipped Arrows", 6, "Time was taken to attach the stone tip to the arrow, and it was not wasted.",)
gtarr = weapons ("Glass Tipped Arrows", 8, "Shard of glass leads the arrow through even the toughest hide.",)
ibarr = weapons ("Iron Barred Arrows", 10, "Iron flares out from the tip of the arrow, forming jagged edges that tear flesh easily.",)

#Staff
10
17
24
30


#Throwing weapons
throki = weapons ("Iron Throwing Knife", 5, "A small iron knife that is prefectly balanced for throwing away.",)
throks = weapons ("Steel Throwing Knife", 7, "Better made than it's iron counterparts. Plus the point is the sharpiest part on it.",)
throai = weapons ("Iron Throwing Axe", 4, "Often mistaken for a handaxe, this axe is made to be thrown and not for campfires.",)
throkas = weapons ("Steel Throwing Axe", 6, "Heavier than the iron verison of it makes throwing it harder, yet if it hits the mark. It will embed itself in much better.",)


#Wards
wards = magic ("Ward",) 
absward = magic ("Absolute Ward",)
shward = magic ("Shield Ward",)
counterward = magic ("Counter Ward",)

#Magic
arcaneb = magic ("Arcane Blast",)
arcaneh = magic ("Arcane Hammer",)
arcanej = magic ("Arcane Javelin",)
arcanep = magic ("Arcane Pluse",)
purems = magic ("Pure Magic Slash",)
curse = magic ("Curse",)
cleanse = magic ("Cleanse",)
cloak = magic ("Cloak",)
sesnecon = magic ("Sesne Confusion",)
lightb = magic ("Light Blast",)

#Armor


#Attacks
arrw = attack ("Arrow",)
slash = attack ("Slash",)
jab = attack ("Jab",)
throwa = attack ("Throwing Axe".)
stab = attack ("Stab",)
bash = attack ("Bash",)
pierce = attack ("Pierce",)
throwk = attack ("Throwing Knife",)
