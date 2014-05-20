class Posicao:
	def __init__(self,x,y):
		self.x = x
		self.y = y


class Componente:
	def __init__(self, cor, posicao,visitado = False, custo = 1, avaliacao):
		self.cor 		= cor
		self.posicao 	= posicao
		self.visitado 	= visitado
		self.custo 		= custo
		self.avaliacao 	= avaliacao
