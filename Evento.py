##@class Evento 
# @brief Breve explicacação pra que a classe serve.
# 
# Mais explicações sobre por que a classe foi criada e uma explicação geral do que ela faz.
class Evento:
    
	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @param tipo ...explicação...
	# @param tempo ...explicação...
	# @param evento_id ...explicação...
    def __init__(self, tipo, tempo, rodada_id): #evento_id
        self.tipo = tipo
        self.tempo = tempo
        self.rodada = rodada_id

	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @return ...explicar o que essa função retorna...
    def __repr__(self):
        return "\nID => " + str(self.evento_id) + "\nTipo => " + self.tipo + "\ntempo => " + str(self.tempo) + "\n"
