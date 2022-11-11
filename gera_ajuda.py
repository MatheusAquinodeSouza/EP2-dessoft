def gera_ajuda(dic_questao):
    lista=[]
    for questao, resposta in dic_questao['opcoes'].items():
        if questao!=dic_questao['correta']:
            lista.append(resposta)
    sort=random.randint(1,2)
    mod=random.sample(lista, sort)
    dica='DICA:\n'
    dica += 'Opções certamente erradas:' + ' | '.join(mod)
    return dica
