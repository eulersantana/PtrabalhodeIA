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

def verificarParede(posicao):
    for tab in tabuleiro:
        if tab.posicao.x == posicao.x:
            if tab.posicao.y == posicao.y:
                if tab.cor == 'cinza':
                    return False
    return True

def posicaoOcupada(posicao, nPontos):
    """
    Verifica sobreposicao de pontos
    """

    if len(nPontos):
        return True
    else:
        for nP in nPontos:
            if nP.posicao.x == posicao.x and nP.posicao.y == posicao.y:
                return False

    return True

def buscaCega(estadoInicial, tabuleiro):
    caminho = []
    for pos in tabuleiro:
        pass      

tabuleiro = [
    '_', 'X', '_',
    'o', 's', 's',
    'X', 'o', 'os',
]

def geraArvore():
    calcFilhos(estadoInicial)

movimentos = {
    'cima': Bola(0, -1),
    'baixo': Bola(0, 1),
    'esquerda': Bola(-1, 0),
    'direita': Bola(1, 0)
}

def calcFilhos(no):
    for move in ['cima', 'baixo', 'esquerda', 'direita']:
        for bola in bolas:
            nova_bola = bola + movimentos[move]

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




        
>>>>>>> d4b6325919f8d1c5d15db4aea9729ecb2a838d1a


