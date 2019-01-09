d = {'a':['b', 'c', 'd'], 'b':['a', 'c']}

def mais_seguidores(dicionario):
    maximo = 0
    maximizante = ''
    for x, y in dicionario.items():
        if len(y) > maximo:
            maximo = len(y)
            maximizante = x
    return maximizante

print(mais_seguidores(d))