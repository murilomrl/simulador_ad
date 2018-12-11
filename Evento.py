##@class Evento 
# @brief Classe Evento comporta os atributos de um evento.
# 
# Evento será usada nas filas ou pilhas de eventos criadas por Simulador. Foi criada para manter as informações que um evento deve ter.
class Evento:
    

	## Comentário: Método construtor de Evento, recebe e define os parâmetros tipo, tempo e rodada_id.
	# @param self Referência ao próprio objeto.
	# @param tipo Define o tipo do evento, entre chegada, partida e entrada_servico
	# @param tempo Tempo de ocorrência do evento.
	# @param rodada_id ...explicação desse parâmetro...
    def __init__(self, tipo, tempo, rodada_id): #evento_id
        self.tipo = tipo
        self.tempo = tempo
        self.rodada = rodada_id

	## Comentário: Retorna uma string que descreve os atributos de Evento.
	# @param self Referência ao próprio objeto.
	# @return Retorna Uma string contendo o Id da rodada, o tipo do evento e seu tempo de ocorrência.
    def __repr__(self):
        return "\nID => " + str(self.rodada_id) + "\nTipo => " + self.tipo + "\ntempo => " + str(self.tempo) + "\n"
