import random
def sorteia_questao_inedita(dic, nivel, lista):
    sort=random.choice(dic[nivel])
    lista.append(sort)
    return sort
