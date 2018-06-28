class Organism():
    def __init__(self,hp, damage):
        self.hp=int(hp)
        self.dmg=int(damage)
    def take_damage(self, damage):
        self.hp-=damage