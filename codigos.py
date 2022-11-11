def transforma_base(questoes):
    dic = {}
    listafacil = []
    listamedio = []
    listadificil = []
    
    for i in questoes:
        for perg, nivel in i.items():
            if nivel == 'facil':
                listafacil.append(i)

            elif nivel == 'medio':
                listamedio.append(i)
            
            elif nivel == 'dificil':
                listadificil.append(i)
         
    if len(listafacil) != 0:
        dic['facil'] = listafacil

    if len(listamedio) != 0: 
        dic['medio'] = listamedio
    
    if len(listadificil) != 0:
        dic['dificil'] = listadificil

    return dic



def valida_questao(questao):

    erro = {}
    alternativa = ['A', 'B', 'C', 'D']


    if 'titulo' not in questao.keys():
        erro['titulo'] = 'nao_encontrado'
    elif questao['titulo'] == '' or len(questao['titulo'].strip()) == 0 or "/t" in questao['titulo']:
        erro['titulo'] = 'vazio'
    
    nivel = ['facil', 'medio', 'dificil']

    if 'nivel' not in questao.keys():  
        erro['nivel'] = 'nao_encontrado'
    elif questao['nivel'] not in nivel:
        erro['nivel'] = 'valor_errado'
    
    if len(questao.keys()) != 4:
        erro['outro'] = 'numero_chaves_invalido'
        cond = True

    

    cond = True

    if 'opcoes' not in questao.keys():
        erro['opcoes'] = 'nao_encontrado'
        cond = False

    elif len(questao['opcoes'].keys()) != 4:
        erro['opcoes'] = 'tamanho_invalido'
        cond = False

    cond = True

    if 'opcoes' not in questao.keys():
        erro['opcoes'] = 'nao_encontrado'
        cond = False

    elif len(questao['opcoes'].keys()) != 4:
        erro['opcoes'] = 'tamanho_invalido'
        cond = False

    if cond and  questao['opcoes'] == 'chave_invalida_ou_nao_encontrada':
       cond = False

    if cond == True:
        if 'A' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        
        elif 'B' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        elif 'C' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        elif 'D' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        else: 
            for opcao in alternativa:
                if opcao in questao['opcoes'].keys():
                    if questao['opcoes'][opcao] == '' or len(questao['opcoes'][opcao].strip()) == 0 or '/t' in questao['opcoes'][opcao]:
                        if 'opcoes' not in erro:
                            erro['opcoes'] = {}
                        erro['opcoes'][opcao] = 'vazia'
    
    if 'correta' not in questao.keys():
        erro['correta'] = 'nao_encontrado'

    elif questao['correta'] not in alternativa:
        erro['correta'] = 'valor_errado'

    return erro
def valida_questao(questao):

    erro = {}
    alternativa = ['A', 'B', 'C', 'D']


    if 'titulo' not in questao.keys():
        erro['titulo'] = 'nao_encontrado'
    elif questao['titulo'] == '' or len(questao['titulo'].strip()) == 0 or "/t" in questao['titulo']:
        erro['titulo'] = 'vazio'
    
    nivel = ['facil', 'medio', 'dificil']

    if 'nivel' not in questao.keys():  
        erro['nivel'] = 'nao_encontrado'
    elif questao['nivel'] not in nivel:
        erro['nivel'] = 'valor_errado'
    
    if len(questao.keys()) != 4:
        erro['outro'] = 'numero_chaves_invalido'
        cond = True

    

    cond = True

    if 'opcoes' not in questao.keys():
        erro['opcoes'] = 'nao_encontrado'
        cond = False

    elif len(questao['opcoes'].keys()) != 4:
        erro['opcoes'] = 'tamanho_invalido'
        cond = False

    cond = True

    if 'opcoes' not in questao.keys():
        erro['opcoes'] = 'nao_encontrado'
        cond = False

    elif len(questao['opcoes'].keys()) != 4:
        erro['opcoes'] = 'tamanho_invalido'
        cond = False

    if cond and  questao['opcoes'] == 'chave_invalida_ou_nao_encontrada':
       cond = False

    if cond == True:
        if 'A' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        
        elif 'B' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        elif 'C' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        elif 'D' not in questao['opcoes'].keys():
            erro['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        else: 
            for opcao in alternativa:
                if opcao in questao['opcoes'].keys():
                    if questao['opcoes'][opcao] == '' or len(questao['opcoes'][opcao].strip()) == 0 or '/t' in questao['opcoes'][opcao]:
                        if 'opcoes' not in erro:
                            erro['opcoes'] = {}
                        erro['opcoes'][opcao] = 'vazia'
    
    if 'correta' not in questao.keys():
        erro['correta'] = 'nao_encontrado'

    elif questao['correta'] not in alternativa:
        erro['correta'] = 'valor_errado'

    return erro

def valida_questoes(lista):
    lista_erro=[]
    for i in lista:
        valida=valida_questao(i)
        lista_erro.append(valida)
    return lista_erro
import random
def sorteia_questao(dic, nivel):
    sort=random.choice(dic[nivel])
    return sort
import random
def sorteia_questao_inedita(dic, nivel, lista):
    sort=random.choice(dic[nivel])
    lista.append(sort)
    return sort
