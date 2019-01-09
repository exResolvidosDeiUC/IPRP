texto = 'ola eu sou muito tola'

def processa(frase):
    lista = list()
    for i in range(len(frase)):
        lista.append((frase[i], i, 0))
        if lista[-1][0] == lista[-2][0] and i != 0:
            lista[-2][2] += 1
            lista.pop(-1)
    return lista

print(processa(texto))