def questao_para_texto(dicionario,numero):

    var_x = ''
    tracos = '------------------------------------- '
    inicio = 'QUESTAO' + ' ' + str(numero) + '\n\n'
    d = dicionario['titulo'] + '\n\n'
    e = 'RESPOSTAS:\n'

    for letra, texto in dicionario['opcoes'].items():
        var_x += (f'{letra}: {texto}' '\n')
    
    final = tracos + inicio + d + e + var_x

    return final
