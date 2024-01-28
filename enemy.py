import random

class Enemy():
    variation = 5

    def __init__(self, name, lvl, xp, hp, atk, df):
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.hp = hp
        self.atk = atk
        self.df = df

    def atack(self):
        damage = random.randrange(self.atk - self.variation, self.atk + self.variation)
        return damage
    
    def receive_damage(self, dmg):
        damage = dmg - self.df
        self.hp -= damage
        return damage