import pygame
from Cores import cores

def vida_dragao(janela, hp_dragao):
    pygame.draw.rect(janela, cores('preto'), (795, 95, 460, 50))
    hp_max = pygame.Rect(800, 100, hp_dragao, 40)

    if hp_dragao >= 340:
        pygame.draw.rect(janela, cores('verde'), hp_max)
    elif hp_dragao >= 230:
        pygame.draw.rect(janela, cores('amarelo'), hp_max)
    elif hp_dragao >= 120:
        pygame.draw.rect(janela, cores('laranja'), hp_max)
    else:
        pygame.draw.rect(janela, cores('vermelho'), hp_max)

def vida_beatrice(janela, hp_beatrice):
    pygame.draw.rect(janela, cores('preto'), (925, 690, 160, 25))
    hp_max = pygame.Rect(930, 695, hp_beatrice, 15)

    if hp_beatrice >= 110:
        pygame.draw.rect(janela, cores('verde'), hp_max)
    elif hp_beatrice >= 85:
        pygame.draw.rect(janela, cores('amarelo'), hp_max)
    elif hp_beatrice >= 40:
        pygame.draw.rect(janela, cores('laranja'), hp_max)
    else:
        pygame.draw.rect(janela, cores('vermelho'), hp_max)

def vida_vlad(janela, hp_vlad):
    pygame.draw.rect(janela, cores('preto'), (925, 820, 260, 30))
    hp_max = pygame.Rect(930, 825, hp_vlad, 20)

    if hp_vlad >= 180:
        pygame.draw.rect(janela, cores('verde'), hp_max)
    elif hp_vlad >= 125:
        pygame.draw.rect(janela, cores('amarelo'), hp_max)
    elif hp_vlad >= 60:
        pygame.draw.rect(janela, cores('laranja'), hp_max)
    else:
        pygame.draw.rect(janela, cores('vermelho'), hp_max)
