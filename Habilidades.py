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