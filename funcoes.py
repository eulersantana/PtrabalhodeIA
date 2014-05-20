from estado  import *


cor = ["verde","preto","cinza"]
movimentacao = {"cima": 1, "baixo": 2, "direita": 3, "esquerda": 4}
# gerador de estado

def geraEstados(estadoAtual,movimento,tabuleiro):
	novoComponentes = []
	for pos in tabuleiro:
		if mevimento == cima and pos.posicao.y:
			if estadoAtual.componentes[0].posicao.x -1 == pos.posicao.x  and  estadoAtual.componentes[0].posicao.y == pos.posicao.y:
				if len(novoComponentes) > 0:
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




		


