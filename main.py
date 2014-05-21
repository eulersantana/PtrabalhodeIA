Tabuleiro = [           # 6
    '_', 'X', '_',
    'o', 's', 's',
    'X', 'o', 'os'
]

Tabuleiro = [           # 59
    'o', 'o', 'o',
    'X', 's', 'X',
    's', 's', '_'
]

Tabuleiro = [           # 26
    'o', 'o', 's',
    'X', 's', 's',
    'o', '_', 'X'
]


# Tabuleiro = [           # 60
#     'os', 'o', 'X',
#     'os', '_', 'X',
#     's', '_', '_'
# ]

# Tabuleiro = [           # 61
#     'X', 's', '_',
#     'o', 'X', 's',
#     'os', 'o', '_'
# ]

Tabuleiro = [           # 62
    'X', 'X', 'o',
    's', 's', 'os',
    '_', '_', 'o'
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
heuristica = []

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
    id_global = 0

    def __init__(self, pai, move):
        self.bolas = []
        self.pai = pai
        self.move = move
        self.id = Estado.id_global
        self.sucessos = 0
        self.avaliacao = 0


        Estado.id_global += 1

        self.nivel = pai.nivel + 1 if pai else 0

    def add_bola(self, posicao):
        self.bolas.append(posicao)

    def check_sucessos(self):

        for bola in self.bolas:
            if 's' in Tabuleiro[bola.x + bola.y * 3]:
                self.sucessos += 1

    def calcAvaliacao(self):
        self.avaliacao = 3 - self.sucessos

    def __str__(self):
        return "{nivel %d => [%s, %s, %s] %d - %d}" % (self.nivel, self.bolas[0], self.bolas[1], self.bolas[2], self.sucessos,self.avaliacao)

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
    global largura_stash

    estado_inicial.check_sucessos()
    largura_stash.append(estado_inicial)

    print '%10s - %s' % ('inicial', estado_inicial)

    continuar = True

    while continuar:
        print "\n"
        print "no %d" % largura_stash[0].id
        continuar = filho_largura(largura_stash.pop(0))

    solucao = []
    pai = largura_stash[-1]

    # verificar percuso de resolucao
    while pai != estado_inicial:
        solucao.append(pai.move)
        pai = pai.pai

    # colocar solucao ao contrario, do primeiro para o ultimo
    solucao.reverse()

    # printa a solucao
    print "\n"
    print solucao

def filho_largura(no):
    global largura_stash

    # para cada tipo de movimento
    for move, delta_pos in Movimento.items():

        #if Oposto[no.move] == move and no.pai.move == move:
        #    continue

        filho = Estado(no, move)

        def ordena(bola):
            return bola.x * - delta_pos[0] + bola.y * - delta_pos[1]

        ordenado = sorted(no.bolas, key=ordena)

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
        print "%10s - %2d - %s" % (move, filho.id, filho)
        largura_stash.append(filho)

        if filho.sucessos == 3:
            return False

    return True


def busca_A():
    global largura_stash

    estado_inicial.check_sucessos()
    estado_inicial.calcAvaliacao()
    largura_stash.append(estado_inicial)

    print '%10s - %s' % ('inicial', estado_inicial)

    def ordenaA(estado):
        return estado.avaliacao + estado.nivel

    while largura_stash[0].sucessos != 3:
        print "\n"
        print "no %d" % largura_stash[0].id
        filho_A(largura_stash.pop(0))
        largura_stash = sorted(largura_stash, key=ordenaA)

    solucao = []
    pai = largura_stash[0]

    # verificar percuso de resolucao
    while pai != estado_inicial:
        solucao.append(pai.move)
        pai = pai.pai

    # colocar solucao ao contrario, do primeiro para o ultimo
    solucao.reverse()

    # printa a solucao
    print "\n"
    print solucao


def filho_A(no):
    global largura_stash

    # para cada tipo de movimento
    for move, delta_pos in Movimento.items():

        #if Oposto[no.move] == move and no.pai.move == move:
        #    continue

        filho = Estado(no, move)

        def ordena(bola):
            return bola.x * - delta_pos[0] + bola.y * - delta_pos[1]

        ordenado = sorted(no.bolas, key=ordena)

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
        filho.calcAvaliacao()

        print "%10s - %2d - %s" % (move, filho.id, filho)

        largura_stash.append(filho)


def main():
    genTabuleiro()
    busca_A()
    #busca_largura()

if __name__ == '__main__':
    main()
