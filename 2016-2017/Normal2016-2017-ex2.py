texto = 'x22ddd cbba'

def processa(frase):
    lista = list()
    for i in range(len(frase)):
        lista.append((frase[i], i, 0))
        if i != 0 and lista[-1][0] == lista[-2][0]:
            lista[-2] = (lista[-2][0], lista[-2][1], lista[-2][2]+1)
            lista.pop(-1)
    return lista

print(processa(texto))