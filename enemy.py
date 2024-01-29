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
        print(f'{self.name} attacked you for {damage} damage!')
        return damage
    
    def receive_damage(self, dmg):
        damage = dmg - self.df
        self.hp -= damage
        if self.hp <= 0:
            self.die()
            return[True, self.xp]
        print(f'{self.name} received {damage} damage!')        
        return[False, damage]
    
    def die(self):
        print(f'{self.name} died!')

ENEMYS = [
    Enemy('Slime', 1, 10, 10, 7, 0),
    Enemy('Goblin', 3, 40, 20, 13, 4),
    Enemy('Orc', 5, 100, 50, 21, 6),
    Enemy('Dragon', 15, 1000, 500, 43, 23),
]
