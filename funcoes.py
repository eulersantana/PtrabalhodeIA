from estado  import *


cor = ["verde","preto","cinza"]
move = {"cima": [-1,1], "baixo": [1,2], "direita": [1,3], "esquerda": [-1,4]}
# gerador de estado

def definirMovimento(estadoAtual):
	acao = []
	for comp in range estadoAtual.componentes:
def calculaAvaliacao():
	

def buscaCega(estadoInicial,tabuleiro):
	caminho = []
	for pos in tabuleiro:
		pass
		



def geraTabuleiro():	
	tabuleiro = []
	for x in range(0,3):
		for y in range(0,3):
			# barreiras
			if x == 2 and y == 0:
				tabuleiro.append(Componente(cor[2],Posicao(x,y),False))
			elif x == 0 and y == 1:
				tabuleiro.append(Componente(cor[2],Posicao(x,y),False))
			# Solucao
			elif x == 1 and y == 1:
				tabuleiro.append(Componente(cor[0],Posicao(x,y),True))
			elif x == 1 and y == 2:
				tabuleiro.append(Componente(cor[0],Posicao(x,y),True))
			elif x == 2 and y == 2:
				tabuleiro.append(Componente(cor[0],Posicao(x,y),True))
			elif True:	
				tabuleiro.append(Componente(cor[1],Posicao(x,y),False))
	return tabuleiro




		


