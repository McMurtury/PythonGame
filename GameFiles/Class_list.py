class life ():
    def __init__ (self, name, magic, agility, strength, intell, endurance, stamina):
        self.name = name
        self.magic = magic
        self.agility = agility
        self.strength = strength
        self.intell = intell
        self.endurance = endurance
        self.stamina = stamina
        self.maxhp = 0
        self.maxsp = 0
        self.maxmp = 0
        self.hp = 0
        self.sp = 0
        self.mp = 0


class character (life):
    def __init__ (self, name, magic, agility, strength, intell, endurance, stamina, inventSize, gold, gender, clas):
        life.__init__(self, name, magic, agility, strength, intell, endurance, stamina)
        self.inventSize = inventSize
        self.inventP = []
        self.inventA = []
        self.inventW = []
        self.inventQ = []
        self.gold = gold
        self.gender = gender
        self.clas = clas

class item ():
     def __init__ (self, name, image, icon, typ, subtyp, description, value):
          self.name = name
          self.image = image
          self.icon = icon
          self.typ = typ
          self.subtyp = subtyp
          self.description = description
          self.value = value


