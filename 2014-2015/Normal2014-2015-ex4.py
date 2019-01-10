def ficheiros_ordena(ficheiro, ficheiro2):
    f = open(ficheiro, 'r')
    ler = f.readlines()
    f.close()
    lista1 = []
    #criar nova lista com soma adicionada no fim
    for i in range(len(ler)):
        soma = 0
        lista = ler[i].split()
        for j in lista[1:]:
                soma = soma + int(j)
        lista.append(soma)
        lista1.append(lista)
    #ordenar lista
    for i in range(len(lista1)):
        for j in range(len(lista1) - 1):
            if lista1[j][-1] > lista1[j + 1][-1]:
                lista1[j], lista1[j + 1] = lista1[j+1], lista1[j]
                #alternativamente
                #auxiliar = lista1[j]
                #lista1[j] = lista1[j + 1]
                #lista1[j + 1] = auxiliar
    #escrever tudo no ficheiro
    f = open(ficheiro2, 'w')
    for listinhas in lista1:
        f.write(str(listinhas) + '\n')
    f.close()
