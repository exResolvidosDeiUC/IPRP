path = 'C:\\Users\\Francisco\\Desktop\\Git\\Normal\\2016-2017\\pessoas.txt'
path2 = 'C:\\Users\\Francisco\\Desktop\\Git\\Normal\\2016-2017\\casais.txt'
def casais(ficheiro, valor, novo_ficheiro):
    f = open(ficheiro, 'r')
    ler = f.readlines()
    f.close()
    # ordenar por idades (passo desnecessário mas garante que o maximo de casais possíveis é criado)
    for i in range(len(ler)):
        for j in range(len(ler)-1):
            if ler[j].split()[2] > ler[j+1].split()[2]:
                ler[j], ler[j + 1] = ler[j+1], ler[j] #troca de ordem na lista
    machos = list()
    femeas = list()
    #separar machos e femeas em duas listas
    for i in ler:
        if i.split()[1] == 'F':
            femeas.append((i.split()[0], i.split()[2]))
        elif i.split()[1] == 'M':
            machos.append((i.split()[0], i.split()[2]))
    #formar casais
    nova_lista = list()
    for m in machos:
        for f in femeas:
            if abs(int(m[1])-int(f[1])) <= valor:
                nova_lista.append(m[0] + ' ' + f[0] + ' ' + str(abs(int(m[1])-int(f[1]))))
                femeas.remove(f)
                break
    #escrever no novo_ficheiro
    f = open(novo_ficheiro, 'w')
    for i in nova_lista:
        f.write(i + '\n')

casais(path, 22, path2)