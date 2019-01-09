texto = 'x22ddd cbba'

def processa(frase):
    lista = list()
    for i in range(len(frase)):
        lista.append((frase[i], i, 0)) #acrescenta tuplo à lista
        if i != 0 and lista[-1][0] == lista[-2][0]: #se não é a primeira letra e tuplo tem letra igual ao anterior NOTA: trocar a ordem das condições resulta em crash na primeira iteração
            lista[-2] = (lista[-2][0], lista[-2][1], lista[-2][2]+1) #penultimo tuplo é substituido por si próprio mas com numero de repeticoes incrementado
            lista.pop(-1) #ultimo tuplo é removido
    return lista

print(processa(texto))
