class Jogador():
    def __init__(self):
        self.nome = "sem nome"
        self.classe = str()
        self.xp = 0
        self.vida = 0
        self.mana = 0
        self.stamina = 0  
        self.inventario = dict()
        self.item_equipado = None

JOGADOR = Jogador()