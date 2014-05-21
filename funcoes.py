from estado import *

cor = ["verde","preto","cinza"]
move = {"cima": [1,1], "baixo": [1,2], "direita": [1,3], "esquerda": [1,4]}


cor = ["verde", "preto", "cinza"]
move = {
    "cima": [-1, 1],
    "baixo": [1, 2],
    "direita": [1, 3],
    "esquerda": [-1, 4]
}

def definirMovimento(estadoAtual):
    acao = []
    for comp in range estadoAtual.componentes:
        pass

def calculaAvaliacao():
    pass




def buscaCega(estadoInicial, tabuleiro):
    caminho = []
    for pos in tabuleiro:
        pass      

tabuleiro = [
    ['_', 'X', '_'],
    ['o', 's', 's'],
    ['X', 'o', 'os']
]

def geraArvore():
    calcFilhos(estadoInicial)

movimentos = {
    'cima': Bola(0, -1),
    'baixo': Bola(0, 1),
    'esquerda': Bola(-1, 0),
    'direita': Bola(1, 0)
}
def verificarParede(posicao):
	for pA in posicao:
		if tabuleiro[pA.x][pA.y] == 'X':
			return False
	return True

def  retorna():
	if move_to == "cima":
		nnPontos.append(nPontos[0] + movimentos["baixo"])
	if move_to == "baixo":
		nnPontos.append(nPontos[0] - movimentos["cima"])
	if move_to == "direta":
		nnPontos.append(nPontos[0] + movimentos["esquerda"])
	if move_to == "esquerda":
		nnPontos.append(nPontos[0] + movimentos["direita"])

		
	if move_to == "cima":
		nnPontos.append(nPontos[1] + movimentos["baixo"])
	if move_to == "baixo":
		nnPontos.append(nPontos[1] - movimentos["cima"])
	if move_to == "direta":
		nnPontos.append(nPontos[1] + movimentos["esquerda"])
	if move_to == "esquerda":
		nnPontos.append(nPontos[1] + movimentos["direita"])

def posicaoOcupada(nPontos,movi_to):
	nnPontos = []
    if nPontos[0].x == nPontos[1].x and nPontos[0].y == nPontos[1].y:
    	if move_to == "cima":
    		nnPontos.append(nPontos[0] + movimentos["baixo"])
    	if move_to == "baixo":
    		nnPontos.append(nPontos[0] - movimentos["cima"])
    	if move_to == "direta":
    		nnPontos.append(nPontos[0] + movimentos["esquerda"])
    	if move_to == "esquerda":
    		nnPontos.append(nPontos[0] + movimentos["direita"])


    	if move_to == "cima":
    		nnPontos.append(nPontos[1] + movimentos["baixo"])
    	if move_to == "baixo":
    		nnPontos.append(nPontos[1] - movimentos["cima"])
    	if move_to == "direta":
    		nnPontos.append(nPontos[1] + movimentos["esquerda"])
    	if move_to == "esquerda":
    		nnPontos.append(nPontos[1] + movimentos["direita"])


   	if nPontos[1].x == nPontos[2].x and nPontos[1].y == nPontos[2].y:
   		if move_to == "cima":
    		nnPontos.append(nPontos[1] + movimentos["baixo"])
    	if move_to == "baixo":
    		nnPontos.append(nPontos[1] - movimentos["cima"])
    	if move_to == "direta":
    		nnPontos.append(nPontos[1] + movimentos["esquerda"])
    	if move_to == "esquerda":
    		nnPontos.append(nPontos[1] + movimentos["direita"])

    		
    	if move_to == "cima":
    		nnPontos.append(nPontos[2] + movimentos["baixo"])
    	if move_to == "baixo":
    		nnPontos.append(nPontos[2] - movimentos["cima"])
    	if move_to == "direta":
    		nnPontos.append(nPontos[2] + movimentos["esquerda"])
    	if move_to == "esquerda":
    		nnPontos.append(nPontos[2] + movimentos["direita"])

   	if nPontos[0].x == nPontos[2].x and nPontos[0].y == nPontos[2].y:




    

def calcFilhos(no):
	novosPontos = []
    for move in ['cima', 'baixo', 'esquerda', 'direita']:
        for bola in bolas:
            novosPontos.append(bola + movimentos[move])
        if verificarParede(novosPontos):
        	if()



def geraTabuleiro():    
    tabuleiro = []

    for x in tabuleiro:
        if '_' in x: #Vazio
            pass

        if 'X' in x: #Parede
            pass

        if 'o' in x: #Bola
            pass

        if 's' in x: #Solução
            pass


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



