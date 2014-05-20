class Posicao:
	
	def __init__(self,x,y):
		self.x = x
		self.y = y


class Componente:

	def __init__(self, cor, posicao):
		self.cor 		= cor
		self.posicao 	= posicao
		

class Estado:

	def __init__(self, componentes,visitado = False, custo = 1, avaliacao):
		self.componentes 	= componentes		
		self.visitado 		= visitado
		self.custo 			= custo
		self.avaliacao 		= avaliacao