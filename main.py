import pygame

def mostrar_erro(erro_texto):
    print(erro_texto)  
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ERRO - 2D1D Dragao")
    fonte = pygame.font.Font(None, 20)

    linhas = erro_texto.splitlines()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.FINGERDOWN:
                rodando = False

        tela.fill((20, 20, 20))
        y = 10
        for linha in linhas:
            render = fonte.render(linha, True, (255, 80, 80))
            tela.blit(render, (10, y))
            y += 18
        pygame.display.update()

    pygame.quit()


try:
    import Funcao_auxiliar as aux
    import Habilidades as hb
    import Barra_de_vida as pv
    import Textos as txt
    from Dragao_ataques import ataques_dragao
except Exception:
    import traceback
    mostrar_erro(traceback.format_exc())
    import sys
    sys.exit()

def carregar_imagem(caminho, tem_transparencia=True):
    with open(caminho, "rb") as f:
        img = pygame.image.load(f, caminho)
    if tem_transparencia:
        return img.convert_alpha()  
    else:
        return img.convert()  

def carregar_som(caminho):
    with open(caminho, "rb") as f:
        return pygame.mixer.Sound(f)

def carregar_musica(caminho):
    f = open(caminho, "rb")
    pygame.mixer.music.load(f)

def main():
    pygame.init()
    pygame.mixer.init()
    janela = pygame.display.set_mode((1300, 900), pygame.SCALED)
    pygame.display.set_caption('2D1D, "2 DOIDOS E 1 DRAGÃO"')

    vlad_img = {
        "normal" : carregar_imagem('imagens/vlad.png'),
        "atacando": carregar_imagem('imagens/vlad_atacando.png'),
        "morto": carregar_imagem('imagens/vlad_morto.png')
    }
    beatrice_img = {
        "normal" : carregar_imagem('imagens/beatrice.png'),
        "morta" : carregar_imagem('imagens/beatrice_morta.png')
    }
    dragao_img = {
        "normal" : carregar_imagem('imagens/dragao.png'),
        "morto" : carregar_imagem('imagens/dragao_morto.png')
    }

    fogo_grande_img = carregar_imagem('imagens/fogo_grande.png')
    fogo_pequeno_img = carregar_imagem('imagens/fogo_pequeno.png')
    corte_dragao_img = carregar_imagem('imagens/corte_dragao.png')
    fundo_img = carregar_imagem('imagens/fundo.png', tem_transparencia=False)
    menu_img = carregar_imagem('imagens/menu.png', tem_transparencia=False)
    nuvem_img = carregar_imagem('imagens/nuvem.png')
    token_beatrice = carregar_imagem('imagens/beatrice_token.png')
    token_vlad = carregar_imagem('imagens/vlad_token.png')
    historia_img = carregar_imagem('imagens/historia.png', tem_transparencia=False)
    escudo_img = carregar_imagem('imagens/escudo.png')
    fada_img = carregar_imagem('imagens/fada.png')
    livro_img = carregar_imagem('imagens/livro.png')
    ganhou_img = carregar_imagem('imagens/ganhou.png', tem_transparencia=False)
    perdeu_img = carregar_imagem('imagens/perdeu.png', tem_transparencia=False)

    som_rugido = carregar_som('audio/Rugido.ogg')
    som_corte_aereo = carregar_som('audio/estalo.ogg')
    som_raio = carregar_som('audio/choque.ogg')
    som_fogo = carregar_som('audio/fogo.ogg')
    som_espada = carregar_som('audio/fuum.ogg')
    som_sapo = carregar_som('audio/sapo.ogg')
    som_fada = carregar_som('audio/fada.ogg')
    som_escudo = carregar_som('audio/escudo.ogg')
    vlad_morte = carregar_som('audio/steve.ogg')
    beatrice_morte = carregar_som('audio/morte_do_roblox.ogg')
    roger_morte = carregar_som('audio/cachorro_chorando.ogg')
    
    
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

    limiar_vlad = [(180, 'verde'), (125, 'amarelo'), (60, 'laranja')]
    limiar_beatrice = [(110, 'verde'), (85, 'amarelo'), (40, 'laranja')]
    limiar_dragao = [(340, 'verde'), (230, 'amarelo'), (120, 'laranja')]


    clock = pygame.time.Clock()
    jogar = True
    ultimo_clique = 0  

    while jogar:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                jogar = False

            if events.type == pygame.MOUSEBUTTONDOWN:
                agora = pygame.time.get_ticks()
                if agora - ultimo_clique < 300:
                    continue  
                ultimo_clique = agora

                if turno in ["menu", "historia", "inicio", "vlad_mensagem", "beatrice_mensagem", "dragao_mensagem", 
                             "vlad_morto", "beatrice_morta", "herois_mortos", "dragao_morto", "perdeu"]:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))

                elif turno == "vlad_escolha" or turno == "beatrice_escolha":
                    pos = pygame.mouse.get_pos()
                    nova_escolha = 1 if pos[1] > 700 else 0
                    if nova_escolha == escolha:
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
                    else:
                        escolha = nova_escolha

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
                        escolha = -1

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
                        escolha = -1
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
                            escolha = -1
                        else:
                            turno = "vlad_morto"

                elif turno == "vlad_morto":
                    if events.key == pygame.K_RETURN:
                        turno = "beatrice_escolha"
                        escolha = -1

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
            carregar_musica('musicas/pixel-pursuit.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
            musica_parou = True

            
        if turno != "menu" and turno != "historia" and turno != "perdeu" and turno != "ganhou":
            janela.blit(fundo_img, (0,0))

            if hp_dragao > 0:
                janela.blit(dragao_img["normal"], (630, 30))
            else:
                janela.blit(dragao_img["morto"], (630, -60))

            if hp_vlad > 0:
                if xvlad < 600:
                    janela.blit(vlad_img["normal"], (xvlad, 250))
                elif xvlad > 650 and xvlad < 700:
                    janela.blit(vlad_img["atacando"], (xvlad, 250))
            else:
                janela.blit(vlad_img["morto"], (xvlad, 250))
            
            if hp_beatrice > 0:
                janela.blit(beatrice_img["normal"], (0, 290))
            else:
                janela.blit(beatrice_img["morta"], (0, 290))


            if turno == "vlad_escolha" or turno == "beatrice_escolha":
                pygame.draw.rect(janela, aux.cores('marrom'), (400, 650, 385, 160))

            janela.blit(token_beatrice, (925, 600))
            janela.blit(token_vlad, (925, 730))

            pv.desenhar_barra_de_vida(janela, hp_dragao, (800, 100), (450, 40), limiar_dragao)

            txt.escrever("VLAD", (1025, 750), janela, 'azul')
            txt.escrever(f"({int(hp_vlad)}/250)", (1020, 780), janela, 'branco')
            pv.desenhar_barra_de_vida(janela, hp_vlad, (930, 825), (250, 20), limiar_vlad)

            txt.escrever("BEATRICE", (1025, 620), janela, 'roxo')
            txt.escrever(f"({int(hp_beatrice)}/150)", (1020, 650), janela, 'branco')
            pv.desenhar_barra_de_vida(janela, hp_beatrice, (930, 695), (150, 15), limiar_beatrice)

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
            txt.escrever("Clique ENTER", (520, 700), janela, 'branco')
            txt.escrever("para começar", (520, 720), janela, 'branco')


        elif turno == "historia":
            janela.blit(historia_img, (0, 0))
            janela.blit(livro_img, (500, 90))
            txt.historia_inicial(janela)


        if turno == "inicio":
            txt.escrever("UM GRANDE DRAGÃO SE APROXIMA!", (60, 630), janela, 'branco')


        if turno == "vlad_escolha":
            txt.texto_vlad_escolha(janela)

            if escolha == 0:
                pygame.draw.rect(janela, aux.cores('azul'), (85, 675, 150, 40), 5)
                txt.texto_vlad_ataque(janela)

            if escolha == 1:    
                pygame.draw.rect(janela, aux.cores('azul'), (85, 735, 310, 40), 5)
                txt.texto_vlad_defesa(janela)


        if turno == "vlad_ataque":
            xvlad, completo = hb.vlad_ataque(xvlad)

            if 650 < xvlad < 660:
                som_tocou = aux.tocar_uma_vez(som_espada, som_tocou)

            if completo:
                hp_dragao -= 25 
                turno = "vlad_mensagem"
        
        if turno == "vlad_defesa":
            tempo = hb.vlad_defesa(tempo)

            if tempo < 100: 
                som_tocou = aux.tocar_uma_vez(som_escudo, som_tocou)

            turno = "vlad_mensagem"

        if escudo_vlad:
            redução = 15
            janela.blit(escudo_img, (300, 300))

        if not escudo_vlad:
            redução = 0

        if turno == "vlad_mensagem":
            if escolha == 0:
                txt.escrever("VLAD ATACOU COM SUA ESPADA!", (60, 630), janela, 'branco')

            elif escolha == 1:
                txt.escrever("VLAD INVOCOU O ESCUDO!", (60, 630), janela, 'branco')


        if turno == "beatrice_escolha":
            txt.texto_beatrice_escolha(janela)

            if escolha == 0:
                pygame.draw.rect(janela, aux.cores('roxo'), (85, 675, 130, 40), 5)
                txt.texto_beatrice_ataque(janela)

            if escolha == 1:    
                pygame.draw.rect(janela, aux.cores('roxo'), (85, 735, 270, 40), 5)
                txt.texto_beatrice_defesa(janela)

        if turno == "beatrice_ataque":
            tempo, nuvem, completo = hb.beatrice_ataque(tempo)

            if tempo < 100:
                som_tocou = aux.tocar_uma_vez(som_raio, som_tocou)

            if completo:
                hp_dragao -= 30
                turno = "beatrice_mensagem"
        
        if turno == "beatrice_defesa":             
            tempo, fada, completo = hb.beatrice_defesa(tempo)

            if tempo < 90:
                som_tocou = aux.tocar_uma_vez(som_fada, som_tocou)
            
            if completo:
                efeito_rugido = False
                if hp_beatrice < 150:
                    hp_beatrice += 15
                    
                if hp_vlad < 250:
                    hp_vlad += 15

                turno = "beatrice_mensagem"

        if turno == "beatrice_mensagem":
            if escolha == 0:
                txt.escrever("BEATRICE USOU MAGIA!", (60, 630), janela, 'branco')
            elif escolha == 1:
                txt.escrever("A FADA MÁGICA CUROU O GRUPO!", (60, 630), janela, 'branco')

        if turno == "dragao_mensagem":
            if ataque != 5:
                txt.texto_dragao_ataque(janela, ataque, fraqueza, redução)

            elif ataque == 5:
                som_tocou = aux.tocar_uma_vez(som_rugido, som_tocou)

                txt.texto_dragao_ataque(janela, ataque, fraqueza, redução)

        if turno == "dragao_ataque":
            ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao, \
            mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, completo, efeito_rugido = ataques_dragao(
            ataque, x_fogo_grande, x_fogo_pequeno, x_corte_dragao,
            mov_fogo_grande, mov_fogo_pequeno, mov_corte_dragao, efeito_rugido
            )

            if ataque == 1 or ataque == 2:
                if x_fogo_pequeno == xvlad + 10:
                    som_tocou = aux.tocar_uma_vez(som_fogo, som_tocou)

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
            txt.escrever("VLAD, O CAVALEIRO, ESTÁ MORTO...", (60, 630), janela, 'branco')

        if turno == "beatrice_morta":
            txt.escrever("BEATRICE, A BRUXA, ESTÁ MORTA...", (60, 630), janela, 'branco')

        if turno == "herois_mortos":
            txt.escrever("BEATRICE E VLAD ESTÃO MORTOS...", (60, 630), janela, 'branco')

        if hp_dragao <= 0 and turno != "ganhou":
            turno = "dragao_morto"
            
            roger_morreu = aux.tocar_uma_vez(roger_morte, roger_morreu)

            txt.escrever("ROGER, O DRAGÃO, MORREU!!!", (60, 630), janela, 'branco')
        
        if turno == "ganhou":
            janela.blit(ganhou_img,(0,0))
            txt.texto_vitoria(janela)

            if musica_parou:
                pygame.mixer.music.stop()
                carregar_musica('musicas/vitoria.ogg')
                pygame.mixer.music.play(-1)
                musica_parou = False

        if turno == "perdeu":
            janela.blit(perdeu_img,(0,0))
            txt.texto_derrota(janela)

            if musica_parou:
                pygame.mixer.music.stop()
                carregar_musica('musicas/triste.ogg')
                pygame.mixer.music.play(-1)
                musica_parou = False

        pygame.display.update()
        clock.tick(95)

    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        mostrar_erro(traceback.format_exc())