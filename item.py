class Item():
    def __init__(self, name, atk, df):
        self.name = name
        self.atk = atk
        self.df = df

ITENS = [
    Item("Espada", 4, 1),
    Item("Escudo", 1, 4),
    Item("Capacete", 0, 5),
    Item("Armadura", 0, 10),
    Item("Calça", 0, 5),
]