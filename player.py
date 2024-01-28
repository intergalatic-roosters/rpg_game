import random

NOMES = [
        'Diego', 'Eric', 'Douglas', 'Cleiton', 
        'Juca', 'Marcinho', 'Renato', 
        ]

class Player():
    def __init__(self, name=None, life=100, level=1, current_xp=0, xp_to_lvlup=None, attack=5, defense=3):
        if name:
            self.name = name
        else:
            self.nome = random.choice(NOMES)

        self.life = life
        self.level = level
        self.current_xp = current_xp
        self.xp_to_lvlup = xp_to_lvlup
        self.attack = attack
        self.defense = defense


    def __str__(self):
        return self.nome, self.level


    def attack(self, enemy):
        print(f'{self} just attack {enemy}')


    def move():
        pass


    def loot():
        pass


    def levelup():
        pass