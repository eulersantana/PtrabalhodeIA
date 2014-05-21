Tabuleiro = [
    '_', 'X', '_',
    'o', 's', 's',
    'X', 'o', 'os'
]

Movimentos = {
    'cima': (0, -1),
    'baixo': (0, 1),
    'esquerda': (-1, 0),
    'direita': (1, 0)
}

Sucessos = []

class Posicao(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Posicao(outro.x + bola.x, outro.y + bola.y)

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

class Estado(object):

    def __int__(self):
        self.bolas = []

    def add_bola(self, posicao):
        self.bolas.append(posicao)

    def check_sucesso(self):
        self.sucessos = 0
        for i in range(3):
            if self.bolas[i] == Sucessos[i]:
                self.sucessos += 1

estado_inicial = Estado()

def genTabuleiro():
    for i in range(len(Tabuleiro)):
        if '_' in Tabuleiro[i]:
            pass

        if 'X' in Tabuleiro[i]:
            pass

        if 's' in Tabuleiro[i]:
            Sucessos.append(Posicao(int(i / 3), i % 3))

        if 'o' in Tabuleiro[i]:
            estado_inicial.add_bola(Posicao(int(i / 3), i % 3))

largura_stash = []

def busca_largura():
    gen_filhos(estado_inicial)

def filho_largura(no):
    for move, delta_pos in Movimentos.items():
        for bola in no.bolas: