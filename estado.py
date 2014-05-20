# -*- coding: utf-8 -*-
# Cor = [verde,preto, cinza]
# avaliacao =  quantos estão na posição correta


class Posicao:

	def __init__(self,x,y):
		self.x = x
		self.y = y


class Componente:

	def __init__(self, cor, posicao):
		self.cor 		= cor
		self.posicao 	= posicao
		

class Estado:

	def __init__(self, componentes,visitado, custo , avaliacao,solucao ):
		self.componentes 	= componentes		
		self.visitado 		= visitado
		self.custo 			= custo
		self.avaliacao 		= avaliacao
		self.solucao		= solucao