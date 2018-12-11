class Evento:
    def __init__(self, tipo, tempo, rodada_id): #evento_id
        self.tipo = tipo
        self.tempo = tempo
        self.rodada = rodada_id

    def __repr__(self):
        return "\nID => " + str(self.evento_id) + "\nTipo => " + self.tipo + "\ntempo => " + str(self.tempo) + "\n"
