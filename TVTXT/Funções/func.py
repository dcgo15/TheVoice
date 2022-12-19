class functools:
    def __init__(self, nome: str, nome_sala: str, item: str, funcao: str):
        self.nome_sala = nome_sala
        self.nom = nome
        self.ite = item
        self.funca = funcao


    def light(self):
        self.nome_sala.ite["bg"] = "white"
        self.nome_sala.ite["fg"] = "#121212"

    def dark(self):
        self.nome_sala.item["bg"] = "#121212"
        self.nome_sala.item["fg"] = "white"
        
