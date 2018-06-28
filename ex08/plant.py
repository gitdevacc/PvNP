from organism import Organism
class Plant(Organism):
    def __init__(self, hp, damage):
        super().__init__()
        self.cost=35
        self.powerup=0
    def attack(self, nonplant):
        nonplant.take_damage(self.dmg+self.powerup)
    def apply_powerup(self, card):
        self.powerup+=card.power
    def weaken_powerup(self):
        self.powerup=self.powerup//2
