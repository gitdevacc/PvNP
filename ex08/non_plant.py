from organism import Organism
class Non_Plant(Organism):
    def __init__(self):
        self.worth=20
        self.hp=80
        self.dmg=5
    def attack(self, plant):
        plant.take_damage(self.dmg)
    