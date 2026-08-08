import pygame
from Funcao_auxiliar import cores

def desenhar_barra_de_vida(janela, hp, pos, tamanho, limiares):
    x, y = pos
    largura, altura = tamanho
    pygame.draw.rect(janela, cores('preto'), (x - 5, y - 5, largura + 10, altura + 10))
    barra = pygame.Rect(x, y, hp, altura)
    for limite, cor in limiares:
        if hp >= limite:
            pygame.draw.rect(janela, cores(cor), barra)
            break
    else:
        pygame.draw.rect(janela, cores('vermelho'), barra)