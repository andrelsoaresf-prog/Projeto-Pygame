from random import randint

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