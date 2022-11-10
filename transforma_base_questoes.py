
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
