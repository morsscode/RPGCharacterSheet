#   spell class for potentially setting up gameplay elements later
class spell:
    def __init__(self, name, damage, cost, type):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.type = type