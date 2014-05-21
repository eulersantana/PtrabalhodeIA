Tabuleiro = [
    '_', 'X', '_',
    'o', 's', 's',
    'X', 'o', 'os'
]

Movimento = {
    'cima': (0, -1),
    'baixo': (0, 1),
    'esquerda': (-1, 0),
    'direita': (1, 0)
}

Oposto = {
    'cima': 'baixo',
    'baixo': 'cima',
    'esquerda': 'direita',
    'direita': 'esquerda',
    '': ''
}

Sucessos = []

class Posicao(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_valido(self, outras):
        if self.x < 0 or self.y < 0 or self.x > 2 or self.y > 2:
            return False

        if Tabuleiro[self.x + self.y * 3] == 'X':
            return False

        for bola in outras:
            if bola == self:
                return False

        return True

    def __add__(self, outro):
        return Posicao(outro.x + self.x, outro.y + self.y)

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

class Estado(object):

    def __init__(self, pai, move):
        self.bolas = []
        self.pai = pai
        self.move = move

    def add_bola(self, posicao):
        self.bolas.append(posicao)

    def check_sucessos(self):
        self.sucessos = 0
        for bola in self.bolas:
            if 's' in Tabuleiro[bola.x + bola.y * 3]:
                self.sucessos += 1

    def __str__(self):
        return "{[%s, %s, %s] %d}" % (self.bolas[0], self.bolas[1], self.bolas[2], self.sucessos)

estado_inicial = Estado(None, '')

def genTabuleiro():
    for i in range(len(Tabuleiro)):
        if '_' in Tabuleiro[i]:
            pass

        if 'X' in Tabuleiro[i]:
            pass

        if 's' in Tabuleiro[i]:
            pass

        if 'o' in Tabuleiro[i]:
            estado_inicial.add_bola(Posicao(i % 3, int(i / 3)))

largura_stash = []

def busca_largura():
    estado_inicial.check_sucessos()
    largura_stash = [estado_inicial]

    print estado_inicial

    while largura_stash:
        filho_largura(largura_stash.pop(0))

def filho_largura(no):
    # para cada tipo de movimento
    for move, delta_pos in Movimento.items():

        if Oposto[no.move] == move:
            continue

        filho = Estado(no, move)
        ordenado = sorted(no.bolas, key=lambda bola: bola.x * - delta_pos[0] * bola.y * - delta_pos[1])

        igual_pai = 0

        for bola in ordenado:
            nova_bola = bola + Posicao(*delta_pos)

            if nova_bola.is_valido(filho.bolas):
                filho.add_bola(nova_bola)
            else:
                igual_pai += 1
                filho.add_bola(bola)

        if igual_pai == 3:
            continue

        filho.check_sucessos()

        if filho.sucessos != 3:
            largura_stash.append(filho)

        print filho

def main():
    genTabuleiro()
    busca_largura()

if __name__ == '__main__':
    main()
