import pygame
import sys
import time
from cobrinha import Cobra
from comida import Comida

pygame.font.init()
minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)

pygame.init()
TAM_TELA = (300,400)
tela = pygame.display.set_mode(TAM_TELA)
tempo = pygame.time.Clock()
pontuacao = 0
cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao

while True:
    tela.fill((7,0,35))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cobra.muda_direcao('DIREITA')
            if event.key == pygame.K_LEFT:
                cobra.muda_direcao('ESQUERDA')
            if event.key == pygame.K_UP:
                cobra.muda_direcao('CIMA')
            if event.key == pygame.K_DOWN:
                cobra.muda_direcao('BAIXO')

    posicao_comida = comida.gera_nova_comida()
    if cobra.move(posicao_comida):
        comida.devorada = True
        pontuacao += 1
        velocidade += 1

    if cobra.verifica_colisao():
        pontos = minha_fonte.render(f'{pontuacao}', True, (255, 255, 255))
        tela.blit(pontos, (10, 10))
        voce_perdeu = minha_fonte.render(f'Você perdeu!', True, (255, 255, 255))
        tela.blit(voce_perdeu, (80, 180))
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()

    pontos = minha_fonte.render(f'{pontuacao}', True, (255, 255, 255))
    tela.blit(pontos, (10, 10))

    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(255,204,0),
                                pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(tela, pygame.Color(255,0,0),
                        pygame.Rect(posicao_comida[0], posicao_comida[1],10,10))
    
    pygame.display.update()

    velocidade = 15
    tempo.tick(velocidade)