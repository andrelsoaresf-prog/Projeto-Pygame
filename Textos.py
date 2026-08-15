import pygame
from Funcao_auxiliar import cores

pygame.font.init()

with open("fontes/pixelado.ttf", "rb") as _arquivo_fonte:
    FONTE_PADRAO = pygame.font.Font(_arquivo_fonte, 20)

def escrever(texto, coordenada, janela, cor, fonte=FONTE_PADRAO):
    if texto == "":
        return
    msg = fonte.render(texto, True, cores(cor))
    janela.blit(msg, coordenada)

def historia_inicial(janela):
    escrever("EM UM LUGAR MUITO DISTANTE, UMA BRUXA AMBICIOSA", (200, 315), janela, 'branco')
    escrever("ESTAVA A PROCURA DE UM GRIMÓRIO RARO COM MAGIAS", (155, 345), janela, 'branco')
    escrever("PODEROSAS PERDIDO NO REINO DE SAPOLÂNDIA. UM HABI-", (155, 375), janela, 'branco')
    escrever("TANTE LOCAL A INFORMOU QUE O GRIMÓRIO FOI TOMADO", (155, 405), janela, 'branco')
    escrever("POR UM TERRÍVEL DRAGÃO.", (155, 435), janela, 'branco')
    escrever("EM OUTRO LUGAR, NESTE MESMO REINO, UM CAVALEIRO", (200, 495), janela, 'branco')
    escrever("ARMADURADO DERROTAVA UM GRUPO DE BANDIDOS E OS", (155, 525), janela, 'branco')
    escrever("QUESTIONAVA SOBRE O SUMIÇO DE SUA IRMÃ. O GRUPO", (155, 555), janela, 'branco')
    escrever("AFIRMOU QUE ELA FOI VISTA AO LADO NORTE DO REINO,", (155, 585), janela, 'branco')
    escrever("REGIÃO HABITADA PELO DRAGÃO.", (155, 615), janela, 'branco')
    escrever("OS DOIS HERÓIS, BEATRICE E VLAD, SE ENCONTRAM", (200, 665), janela, 'branco')
    escrever("NO CAMINHO E DESCOBREM QUE COMPARTILHAM  DO MESMO", (155, 695), janela, 'branco')
    escrever("OBJETIVO: DERROTAR ROGER, O PODEROSO DRAGÃO.", (155, 725), janela, 'branco')

def texto_vlad_escolha(janela):
    escrever("O QUE VLAD, O CAVALEIRO, VAI FAZER?", (60, 610), janela, 'branco')
    escrever("· ATACAR", (60, 685), janela, 'branco')
    escrever("· INVOCAR ESCUDO", (60, 745), janela, 'branco')

def texto_vlad_ataque(janela):
    escrever("VLAD ATACA O DRA-", (410, 660), janela, 'branco')
    escrever("GÃO COM A ESPADA!", (410, 690), janela, 'branco')
    escrever("CAUSA 25 DE DANO", (410, 750), janela, 'vermelho')

def texto_vlad_defesa(janela):
    escrever("VLAD USA O ESCUDO", (410, 660), janela, 'branco')
    escrever("PELO PRÓXIMO TURNO!", (410, 690), janela, 'branco')
    escrever("ABSORVE 15 DE DAN0", (410, 750), janela, 'amarelo')

def texto_beatrice_escolha(janela):
    escrever("O QUE BEATRICE, A BRUXA, VAI FAZER?", (60, 610), janela, 'branco')
    escrever("· MAGIA", (60, 685), janela, 'branco')
    escrever("· INVOCAR FADA", (60, 745), janela, 'branco')

def texto_beatrice_ataque(janela):
    escrever("UM RAIO É INVOCADO", (410, 660), janela, 'branco')
    escrever("SOBRE O DRAGÃO!", (410, 690), janela, 'branco')
    escrever("CAUSA 30 DE DANO", (410, 750), janela, 'vermelho')

def texto_beatrice_defesa(janela):
    escrever("UMA FADA MÁGICA OS", (410, 660), janela, 'branco')
    escrever("FORTALECEM!", (410, 690), janela, 'branco')
    escrever("CURA 15 DE VIDA DE", (410, 720), janela, 'verde')
    escrever("CADA UM E ANULA", (410, 750), janela, 'verde')
    escrever("EFEITOS NEGATIVOS", (410, 780), janela, 'verde')

def texto_dragao_ataque(janela, ataque, fraqueza, redução):
    if (ataque == 1 or ataque == 2):
        escrever("ROGER, O DRAGÃO, SOLTOU UM FOGO PE-", (60, 630), janela, 'branco')
        escrever("QUENO!", (60, 660), janela, 'branco')
        escrever(f"(CAUSOU {int(25*fraqueza-redução)} DE DANO NO VLAD)", (60, 720), janela, 'branco')

    elif(ataque == 3 or ataque == 4):
        escrever("ROGER, O DRAGÃO, FEZ CORTE AÉREO!", (60, 630), janela, 'branco')
        escrever(f"(CAUSOU {int(25*fraqueza-redução)} DE DANO EM AMBOS)", (60, 690), janela, 'branco')

    elif(ataque == 5):
        escrever("ROGER, O DRAGÃO, RUGIU!", (60, 630), janela, 'branco')
        escrever("(VLAD E BEATRICE ESTÃO FRAGILIZADOS", (60, 690), janela, 'branco')
        escrever(" E RECEBERÃO MAIS DANO!!!!)", (60, 720), janela, 'branco')

    elif(ataque == 6):
        escrever("ROGER, O DRAGÃO, SOLTOU FOGO GRANDE!", (60, 630), janela, 'branco')
        escrever(f"(CAUSOU {int(35*fraqueza-redução)} DE DANO EM AMBOS)", (60, 690), janela, 'branco')

def texto_vitoria(janela):
    escrever("AO DERROTAR O DRAGÃO, VLAD AVISTA SUA IRMÃ LOGO À FRENTE", (105, 560), janela, 'branco')
    escrever("E A ABRAÇA, TRAZENDO-A SÃ E SALVA PARA CASA.", (80, 590), janela, 'branco')
    escrever("BEATRICE ENCONTROU O GRIMÓRIO NAS CAVERNAS DO DRAGÃO E", (105, 650), janela, 'branco')
    escrever("COM ELE SE TORNOU UMA BRUXA SÁBIA E PODEROSA, NUNCA", (80, 680), janela, 'branco')
    escrever("ESQUECENDO DO AMIGO QUE A AJUDOU.", (80, 710), janela, 'branco')
    escrever("DESDE ENTÃO, ELES SEMPRE VÃO JUNTOS EM SUAS AVENTURAS.", (105, 780), janela, 'branco')

    escrever("ENTER para sair do jogo", (400, 870), janela, 'branco')

def texto_derrota(janela):
    escrever("INFELIZMENTE, OS DOIS HERÓIS TIVERAM UM TRISTE FIM...", (105, 560), janela, 'branco')
    escrever("O DRAGÃO PERMANECE GUARDANDO O GRIMÓRIO MISTERIOSO...", (105, 620), janela, 'branco')
    escrever("E A IRMÃ DO VLAD CONTINUA DESAPARECIDA...", (105, 680), janela, 'branco')

    escrever("ENTER para tentar novamente", (400, 870), janela, 'branco')


