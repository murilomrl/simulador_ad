##@class Fregues 
# @brief Breve explicacação pra que a classe serve.
# 
# Mais explicações sobre por que a classe foi criada e uma explicação geral do que ela faz.
class Fregues:
	
	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @param chegada ...explicação...
	# @param servico ...explicação...
	# @param tipo ...explicação...	
	def __init__(self,chegada,servico,tipo):
		self.chegada = chegada
		self.servico = servico
		self.tipo = tipo
		
		
	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @return...explicar o que essa função retorna...
	def __repr__(self):
		return "chegada => " + str(self.chegada) + "\nservico => " + str(self.servico) + "\ntipo => " + str(self.tipo) + "\n"
		
		
	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @return...explicar o que essa função retorna...
	def get_tipo(self):
		return self.tipo
		
		
	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @return...explicar o que essa função retorna...
	def get_servico(self):
		return self.servico
		
		
	## Comentário: explicar o que o método faz.
	# @param self ...explicação...
	# @return...explicar o que essa função retorna...
	def get_chegada(self):
		return self.chegada
