def hi():
    print("hello")

class character:
    def __init__(self, name, species, cClass):
        self.name = name
        self.species = species
        self.cClass = cClass
        self.spells = []
        self.damage = 0
        self.health = 100

        #if cClass == 'wizard':
        #    self.spells.append('heal')
        #    self.spells.append('fireball')
    def display(self):
        print("name: " + self.name)
        print("species: " + self.species)
        print("class: " + self.cClass)
        print("spells: ")
        for spell in self.spells:
            print(spell.name)
