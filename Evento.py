class Evento:
	def __init__(self, tipo, tempo, evento_id):
		self.tipo = tipo
		self.tempo = tempo
		self.evento_id = evento_id

	def __repr__(self):
		return "\nID => " + str(self.evento_id) + "\nTipo => " + self.tipo + "\ntempo => " + str(self.tempo) + "\n"