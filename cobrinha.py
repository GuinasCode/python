class Cobra:
    def __init__(self, tam_tela=(300,400),
                        posicao=[80,50],
                        corpo=[[80,50], [70,50], [60,50]],
                        direcao='DIREITA'):
        self.tam_tela = tam_tela
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = 'DIREITA'

    def muda_direcao(self, nova_direcao):
        if nova_direcao == 'DIREITA' and not self.direcao == 'ESQUERDA':
            self.direcao = 'DIREITA'
        if nova_direcao == 'ESQUERDA' and not self.direcao == 'DIREITA':
            self.direcao = 'ESQUERDA'
        if nova_direcao == 'CIMA' and not self.direcao == 'BAIXO':
            self.direcao = 'CIMA'
        if nova_direcao == 'BAIXO' and not self.direcao == 'CIMA':
            self.direcao = 'BAIXO'

    def move(self, posicao_comida):
        if self.direcao == 'DIREITA':
            self.posicao[0] += 10
        if self.direcao == 'ESQUERDA':
            self.posicao[0] -= 10
        if self.direcao == 'BAIXO':
            self.posicao[1] += 10
        if self.direcao == 'CIMA':
            self.posicao[1] -= 10

        self.corpo.insert(0, list(self.posicao))
        if self.posicao == posicao_comida:
            return True
        self.corpo.pop()


    def verifica_colisao(self):
        if self.posicao[0] > (self.tam_tela[0]-10) or self.posicao[0] < 0:
            return True
        if self.posicao[1] > (self.tam_tela[1]-10) or self.posicao[1] < 0:
            return True
        for parte_do_corpo in self.corpo[1:]:
            if self.posicao == parte_do_corpo:
                return True