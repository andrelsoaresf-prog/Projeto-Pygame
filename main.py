import pygame
from Cores import cores
from random import randint

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


def ataques_dragao(ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao,
                   mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, efeito_rugido):

    if ataque is None:
        ataque = randint(1, 6)

        if ataque == 6:
            mov_fogo_grande = True
            x_fogo_grande = 700

        elif ataque == 3 or ataque == 4:
            mov_corte_dragao = True
            x_corte_dragao = 800

        elif ataque == 1 or ataque == 2:
            mov_fogo_pequeno = True
            x_fogo_pequeno = 800

        elif ataque == 5:
            efeito_rugido = True
            return ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao, \
                   mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, True, efeito_rugido

    completo = False

    if mov_fogo_grande:
        x_fogo_grande -= 10
        if x_fogo_grande < -100:
            mov_fogo_grande = False
            completo = True

    if mov_fogo_pequeno:
        x_fogo_pequeno -= 10
        if x_fogo_pequeno < 150:
            mov_fogo_pequeno = False
            completo = True

    if mov_corte_dragao:
        x_corte_dragao -= 20
        if x_corte_dragao < -100:
            mov_corte_dragao = False
            completo = True

    return ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao, \
           mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, completo, efeito_rugido

def escrever(texto, coordenada, janela, cor):
    msg = pygame.font.Font("fontes/pixelado.ttf", 20).render(texto, True, cores(cor))
    janela.blit(msg, coordenada)

def vlad_ataque(xvlad):
    if xvlad < 650:
        xvlad += 15
    else:
        xvlad += 2

    if 100 < xvlad <= 700:
        return xvlad, False
    else:
        return 100, True

def vlad_defesa(tempo):
    tempo += 5
    if 5 <= tempo <= 100:
        return tempo
    else:
        return 0

def beatrice_ataque(tempo):
    tempo += 5
    if 5 <= tempo <= 100:
        return tempo, True, False
    else:
        return 0, False, True

def beatrice_defesa(tempo):
    tempo += 1
    if tempo <= 100:
        return tempo, True, False
    else:
        return 0, False, True


def main():
    pygame.init()
    pygame.mixer.init()
    janela = pygame.display.set_mode((1300, 900))
    pygame.display.set_caption('2D1D, "2 DOIDOS E 1 DRAGÃO"')

    vlad_img = [
        pygame.image.load('imagens/vlad.png'),
        pygame.image.load('imagens/vlad_atacando.png'),
        pygame.image.load('imagens/vlad_morto.png')
    ]
    beatrice_img = [
        pygame.image.load('imagens/beatrice.png'),
        pygame.image.load('imagens/beatrice_morta.png')
    ]
    dragao_img = [
        pygame.image.load('imagens/dragao.png'),
        pygame.image.load('imagens/dragao_morto.png')
    ]

    fogo_grande_img = pygame.image.load('imagens/fogo_grande.png')
    fogo_pequeno_img = pygame.image.load('imagens/fogo_pequeno.png')
    corte_dragao_img = pygame.image.load('imagens/corte_dragao.png')
    fundo_img = pygame.image.load('imagens/fundo.png')
    menu_img = pygame.image.load('imagens/menu.png')
    nuvem_img = pygame.image.load('imagens/nuvem.png')
    token_beatrice = pygame.image.load('imagens/beatrice_token.png')
    token_vlad = pygame.image.load('imagens/vlad_token.png')
    historia_img = pygame.image.load('imagens/historia.png')
    escudo_img = pygame.image.load('imagens/escudo.png')
    fada_img = pygame.image.load('imagens/fada.png')
    livro_img = pygame.image.load('imagens/livro.png')
    ganhou_img = pygame.image.load('imagens/ganhou.png')
    perdeu_img = pygame.image.load('imagens/perdeu.png')

    som_rugido = pygame.mixer.Sound('audio/Rugido.mp3')
    som_corte_aereo = pygame.mixer.Sound('audio/estalo.mp3')
    som_raio = pygame.mixer.Sound('audio/choque.mp3')
    som_fogo = pygame.mixer.Sound('audio/fogo.mp3')
    som_espada = pygame.mixer.Sound('audio/fuum.mp3')
    som_sapo = pygame.mixer.Sound('audio/sapo.mp3')
    som_fada = pygame.mixer.Sound('audio/fada.mp3')
    som_escudo = pygame.mixer.Sound('audio/escudo.mp3')
    vlad_morte = pygame.mixer.Sound('audio/steve.mp3')
    beatrice_morte = pygame.mixer.Sound('audio/morte_do_roblox.mp3')
    roger_morte = pygame.mixer.Sound('audio/cachorro_chorando.mp3')
    
    
    hp_dragao = 450
    x_fogo_grande = 1500
    x_fogo_pequeno = 1500
    x_corte_dragao = 1500
    mov_fogo_grande = False
    mov_fogo_pequeno = False
    mov_corte_dragao = False
    ataque = None
    efeito_rugido = False
    fraqueza = 1

    hp_vlad = 250
    hp_beatrice = 150
    beatrice_morreu = False
    vlad_morreu = False
    roger_morreu = False
    escudo_vlad = False
    nuvem = False
    fada = False
    redução = 0
    xvlad = 100
    escolha = 0
    tempo = 0
    musica_parou = False
    som_tocou = False
    turno_anterior = None
    turno = "menu"


    clock = pygame.time.Clock()
    jogar = True

    while jogar:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                jogar = False

            if events.type == pygame.KEYDOWN:
                if turno == "menu" or turno == "ganhou":
                    if events.key == pygame.K_s:
                        som_sapo.play()

                if turno == "menu":
                    if events.key == pygame.K_RETURN:
                        turno = "historia"

                elif turno == "historia":
                    if events.key == pygame.K_RETURN:
                        turno = "inicio"

                elif turno == "inicio":
                    if events.key == pygame.K_RETURN:
                        turno = "vlad_escolha"
                        escolha = 0

                elif turno == "vlad_escolha":
                    if events.key == pygame.K_UP:
                        escolha = 0
                    if events.key == pygame.K_DOWN:
                        escolha = 1

                    if events.key == pygame.K_RETURN:
                        if escolha == 0:
                            turno = "vlad_ataque"
                        elif escolha == 1:
                            escudo_vlad = True
                            turno = "vlad_defesa"

                elif turno == "vlad_mensagem":
                    if events.key == pygame.K_RETURN:
                        escolha = 0
                        if hp_beatrice > 0:
                            turno = "beatrice_escolha"
                        else:
                            turno = "beatrice_morta"

                elif turno == "beatrice_escolha":
                    if events.key == pygame.K_UP:
                        escolha = 0
                    if events.key == pygame.K_DOWN:
                        escolha = 1

                    if events.key == pygame.K_RETURN:
                        if escolha == 0:
                            turno = "beatrice_ataque"
                        elif escolha == 1:
                            turno = "beatrice_defesa"

                elif turno == "beatrice_mensagem":
                    if events.key == pygame.K_RETURN:
                        escolha = 0
                        turno = "dragao_ataque"

                elif turno == "dragao_mensagem":
                    if events.key == pygame.K_RETURN:
                        ataque = None
                        escudo_vlad = False

                        if hp_vlad <= 0 and hp_beatrice <= 0:
                            turno = "herois_mortos"
                        elif hp_vlad > 0:
                            turno = "vlad_escolha"
                        else:
                            turno = "vlad_morto"

                elif turno == "vlad_morto":
                    if events.key == pygame.K_RETURN:
                        turno = "beatrice_escolha"

                elif turno == "beatrice_morta":
                    if events.key == pygame.K_RETURN:
                        turno = "dragao_ataque"

                elif turno == "herois_mortos":
                    if events.key == pygame.K_RETURN:
                        turno = "perdeu"

                elif turno == "dragao_morto":
                    if events.key == pygame.K_RETURN:
                        turno = "ganhou"

                elif turno == "perdeu":
                    if events.key == pygame.K_RETURN:
                        hp_dragao = 450
                        hp_vlad = 250
                        hp_beatrice = 150
                        turno = "inicio"

                elif turno == "ganhou":
                    if events.key == pygame.K_RETURN:
                        jogar = False

        if turno != turno_anterior:
            som_tocou = False
            turno_anterior = turno

        if not musica_parou and turno != "ganhou" and turno != "perdeu":
            pygame.mixer.music.load('musicas/pixel-pursuit.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
            musica_parou = True

            
        if turno != "menu" and turno != "historia" and turno != "perdeu" and turno != "ganhou":
            janela.blit(fundo_img, (0,0))

            if hp_dragao > 0:
                janela.blit(dragao_img[0], (630, 30))
            else:
                janela.blit(dragao_img[1], (630, -60))

            if hp_vlad > 0:
                if xvlad < 600:
                    janela.blit(vlad_img[0], (xvlad, 250))
                elif xvlad > 650 and xvlad < 700:
                    janela.blit(vlad_img[1], (xvlad, 250))
            else:
                janela.blit(vlad_img[2], (xvlad, 250))
            
            if hp_beatrice > 0:
                janela.blit(beatrice_img[0], (0, 290))
            else:
                janela.blit(beatrice_img[1], (0, 290))


            if turno == "vlad_escolha" or turno == "beatrice_escolha":
                pygame.draw.rect(janela, cores('marrom'), (400, 650, 385, 160))

            janela.blit(token_beatrice, (925, 600))
            janela.blit(token_vlad, (925, 730))

            vida_dragao(janela, hp_dragao)

            escrever("VLAD", (1025, 750), janela, 'azul')
            escrever(f"({int(hp_vlad)}/250)", (1020, 780), janela, 'branco')
            vida_vlad(janela, hp_vlad)

            escrever("BEATRICE", (1025, 620), janela, 'roxo')
            escrever(f"({int(hp_beatrice)}/150)", (1020, 650), janela, 'branco')
            vida_beatrice(janela, hp_beatrice)

            if nuvem:
                janela.blit(nuvem_img, (850, 25))
            
            if fada:
                janela.blit(fada_img, (100, 100))

            if mov_fogo_grande: 
                janela.blit(fogo_grande_img, (x_fogo_grande, 230))
        
            if mov_fogo_pequeno:
                janela.blit(fogo_pequeno_img, (x_fogo_pequeno, 250))
        
            if mov_corte_dragao:
                janela.blit(corte_dragao_img, (x_corte_dragao, 300))
        
        elif turno == "menu":
            janela.blit(menu_img, (0, 0))
            escrever("Clique ENTER", (520, 700), janela, 'branco')
            escrever("para começar", (520, 720), janela, 'branco')


        elif turno == "historia":
            janela.blit(historia_img, (0, 0))
            janela.blit(livro_img, (500, 90))
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


        if turno == "inicio":
            escrever("UM GRANDE DRAGÃO SE APROXIMA!", (60, 630), janela, 'branco')


        if turno == "vlad_escolha":
            escrever("O QUE VLAD, O CAVALEIRO, VAI FAZER?", (60, 610), janela, 'branco')
            escrever("· ATACAR", (60, 685), janela, 'branco')
            escrever("· INVOCAR ESCUDO", (60, 745), janela, 'branco')

            if escolha == 0:
                pygame.draw.rect(janela, cores('azul'), (85, 675, 150, 40), 5)
                escrever("VLAD ATACA O DRA-", (410, 660), janela, 'branco')
                escrever("GÃO COM A ESPADA!", (410, 690), janela, 'branco')
                escrever("CAUSA 25 DE DANO", (410, 750), janela, 'vermelho')

            if escolha == 1:    
                pygame.draw.rect(janela, cores('azul'), (85, 735, 310, 40), 5)
                escrever("VLAD USA O ESCUDO", (410, 660), janela, 'branco')
                escrever("PELO PRÓXIMO TURNO!", (410, 690), janela, 'branco')
                escrever("ABSORVE 15 DE DAN0", (410, 750), janela, 'amarelo')


        if turno == "vlad_ataque":
            xvlad, completo = vlad_ataque(xvlad)

            if 650 < xvlad < 660 and not som_tocou:
                som_espada.play()
                som_tocou = True

            if completo:
                hp_dragao -= 25 
                turno = "vlad_mensagem"
        
        if turno == "vlad_defesa":
            tempo = vlad_defesa(tempo)

            if tempo < 100 and not som_tocou:
                som_escudo.play() 
                som_tocou = True

            turno = "vlad_mensagem"

        if escudo_vlad:
            redução = 15
            janela.blit(escudo_img, (300, 300))

        if not escudo_vlad:
            redução = 0

        if turno == "vlad_mensagem":
            if escolha == 0:
                escrever("VLAD ATACOU COM SUA ESPADA!", (60, 630), janela, 'branco')

            elif escolha == 1:
                escrever("VLAD INVOCOU O ESCUDO!", (60, 630), janela, 'branco')


        if turno == "beatrice_escolha":
            escrever("O QUE BEATRICE, A BRUXA, VAI FAZER?", (60, 610), janela, 'branco')

            escrever("· MAGIA", (60, 685), janela, 'branco')
            escrever("· INVOCAR FADA", (60, 745), janela, 'branco')

            if escolha == 0:
                pygame.draw.rect(janela, cores('roxo'), (85, 675, 130, 40), 5)
                escrever("UM RAIO É INVOCADO", (410, 660), janela, 'branco')
                escrever("SOBRE O DRAGÃO!", (410, 690), janela, 'branco')
                escrever("CAUSA 30 DE DANO", (410, 750), janela, 'vermelho')

            if escolha == 1:    
                pygame.draw.rect(janela, cores('roxo'), (85, 735, 270, 40), 5)
                escrever("UMA FADA MÁGICA OS", (410, 660), janela, 'branco')
                escrever("FORTALECEM!", (410, 690), janela, 'branco')
                escrever("CURA 15 DE VIDA DE", (410, 720), janela, 'verde')
                escrever("CADA UM E ANULA", (410, 750), janela, 'verde')
                escrever("EFEITOS NEGATIVOS", (410, 780), janela, 'verde')

        if turno == "beatrice_ataque":
            tempo, nuvem, completo = beatrice_ataque(tempo)

            if tempo < 100 and not som_tocou:
                som_raio.play()
                som_tocou = True

            if completo:
                hp_dragao -= 30
                turno = "beatrice_mensagem"
        
        if turno == "beatrice_defesa":             
            tempo, fada, completo = beatrice_defesa(tempo)

            if tempo < 100 and not som_tocou:
                som_fada.play()
                som_tocou = True
            
            if completo:
                efeito_rugido = False
                if hp_beatrice < 150:
                    hp_beatrice += 15
                    
                if hp_vlad < 250:
                    hp_vlad += 15

                turno = "beatrice_mensagem"

        if turno == "beatrice_mensagem":
            if escolha == 0:
                escrever("BEATRICE USOU MAGIA!", (60, 630), janela, 'branco')
            elif escolha == 1:
                escrever("A FADA MÁGICA CUROU O GRUPO!", (60, 630), janela, 'branco')

        if turno == "dragao_mensagem":
            if ataque == 1 or ataque == 2:
                escrever("ROGER, O DRAGÃO, SOLTOU UM FOGO PE-", (60, 630), janela, 'branco')
                escrever("QUENO!", (60, 660), janela, 'branco')
                escrever(f"(CAUSOU {int(25*fraqueza-redução)} DE DANO NO VLAD)", (60, 720), janela, 'branco')

            elif ataque == 3 or ataque == 4:
                escrever("ROGER, O DRAGÃO, FEZ CORTE AÉREO!", (60, 630), janela, 'branco')
                escrever(f"(CAUSOU {int(25*fraqueza-redução)} DE DANO EM AMBOS)", (60, 690), janela, 'branco')

            elif ataque == 5:
                if not som_tocou:
                    som_rugido.play()
                    som_tocou = True

                escrever("ROGER, O DRAGÃO, RUGIU!", (60, 630), janela, 'branco')
                escrever("(VLAD E BEATRICE ESTÃO FRAGILIZADOS", (60, 690), janela, 'branco')
                escrever(" E RECEBERÃO MAIS DANO!!!!)", (60, 720), janela, 'branco')

            elif ataque == 6:
                escrever("ROGER, O DRAGÃO, SOLTOU FOGO GRANDE!", (60, 630), janela, 'branco')
                escrever(f"(CAUSOU {int(35*fraqueza-redução)} DE DANO EM AMBOS)", (60, 690), janela, 'branco')




        if turno == "dragao_ataque":
            ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao, \
            mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, completo, efeito_rugido = ataques_dragao(
            ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao,
            mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, efeito_rugido
            )

            if ataque == 1 or ataque == 2:
                if x_fogo_pequeno == xvlad + 10 and not som_tocou:
                    som_fogo.play()
                    som_tocou = True

            if completo:
                turno = "dragao_mensagem"

        if x_corte_dragao == xvlad or x_corte_dragao == 0:
            som_corte_aereo.play()
        
        if x_fogo_grande == xvlad or x_fogo_grande == 0 or x_fogo_pequeno == 150:
            som_fogo.play()

        if efeito_rugido:
            fraqueza = 1.25
        if not efeito_rugido:
            fraqueza = 1
        
        if x_fogo_pequeno == 200:
            if hp_vlad > 0:
                hp_vlad -= int(25 * fraqueza - redução)
        
        if x_fogo_grande == 200:
            if hp_vlad > 0:
                hp_vlad -= int(35 * fraqueza - redução)
        if x_fogo_grande == 0:
            if hp_beatrice > 0:
                hp_beatrice -= int(35 * fraqueza - redução)
        
        if x_corte_dragao == 200:
            if hp_vlad > 0:
                hp_vlad -= int(25 * fraqueza - redução)
        if x_corte_dragao == 0:
            if hp_beatrice > 0:
                hp_beatrice -= int(25 * fraqueza - redução)

                

        if hp_vlad <= 0 and not vlad_morreu:
            vlad_morte.play()
            vlad_morreu = True

        if hp_beatrice <= 0 and not beatrice_morreu:
            beatrice_morte.play()
            beatrice_morreu = True

        if turno == "vlad_morto":
            escrever("VLAD, O CAVALEIRO, ESTÁ MORTO...", (60, 630), janela, 'branco')

        if turno == "beatrice_morta":
            escrever("BEATRICE, A BRUXA, ESTÁ MORTA...", (60, 630), janela, 'branco')

        if turno == "herois_mortos":
            escrever("BEATRICE E VLAD ESTÃO MORTOS...", (60, 630), janela, 'branco')

        if hp_dragao <= 0 and turno != "ganhou":
            turno = "dragao_morto"
            
            if not roger_morreu:
                roger_morte.play()
                roger_morreu = True

            escrever("ROGER, O DRAGÃO, MORREU!!!", (60, 630), janela, 'branco')
        
        if turno == "ganhou":
            janela.blit(ganhou_img,(0,0))

            escrever("AO DERROTAR O DRAGÃO, VLAD AVISTA SUA IRMÃ LOGO À FRENTE", (105, 560), janela, 'branco')
            escrever("E A ABRAÇA, TRAZENDO-A SÃ E SALVA PARA CASA.", (80, 590), janela, 'branco')
            escrever("BEATRICE ENCONTROU O GRIMÓRIO NAS CAVERNAS DO DRAGÃO E", (105, 650), janela, 'branco')
            escrever("COM ELE SE TORNOU UMA BRUXA SÁBIA E PODEROSA, NUNCA", (80, 680), janela, 'branco')
            escrever("ESQUECENDO DO AMIGO QUE A AJUDOU.", (80, 710), janela, 'branco')
            escrever("DESDE ENTÃO, ELES SEMPRE VÃO JUNTOS EM SUAS AVENTURAS.", (105, 780), janela, 'branco')

            escrever("ENTER para sair do jogo", (400, 870), janela, 'branco')

            if musica_parou:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('musicas/vitoria.mp3')
                pygame.mixer.music.play(-1)
                musica_parou = False

        if turno == "perdeu":
            janela.blit(perdeu_img,(0,0))

            escrever("INFELIZMENTE, OS DOIS HERÓIS TIVERAM UM TRISTE FIM...", (105, 560), janela, 'branco')
            escrever("O DRAGÃO PERMANECE GUARDANDO O GRIMÓRIO MISTERIOSO...", (105, 620), janela, 'branco')
            escrever("E A IRMÃ DO VLAD CONTINUA DESAPARECIDA...", (105, 680), janela, 'branco')

            escrever("ENTER para tentar novamente", (400, 870), janela, 'branco')

            if musica_parou:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('musicas/triste.mp3')
                pygame.mixer.music.play(-1)
                musica_parou = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()