class Fregues:
	def __init__(self,chegada,servico,tipo):
		self.chegada = chegada
		self.servico = servico
		self.tipo = tipo

	def __repr__(self):
		return "chegada => " + str(self.chegada) + "\nservico => " + str(self.servico) + "\ntipo => " + str(self.tipo) + "\n"

	def get_tipo(self):
		return self.tipo

	def get_servico(self):
		return self.servico

	def get_chegada(self):
		return self.chegada