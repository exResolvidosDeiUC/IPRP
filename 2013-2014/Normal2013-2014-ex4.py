def criar():
    f = open('horarioss.txt', 'w')
    f.write('2 09:00 02:00 LEI1A IPRP-TP1-1 G41\n3 13:00 02:00 LEI1A IPRP-TP1-2 G43')
    f.close()


criar()


def dicio(ficheiro, ficheiro_novo):
    f = open(ficheiro, 'r')
    ler = f.readlines()
    f.close()
    dicio = dict()
    for linha in ler:
        linha = linha.split()
        if dicio.get(linha[-1]) is None:
            dicio[linha[-1]] = [linha]
        else:
            dicio[linha[-1]].append(linha)
        dicio[linha[-1]][-1].pop(-1)

    for chave, valor in dicio.items():
        f = open(ficheiro_novo + chave + '.txt', 'w')
        f.write('Horario da sala' + chave + '\n')
        for aula in valor:
            f.write(aula[0] + ' ' + aula[1] + ' ' + aula[2] + ' ' + aula[3] + ' ' + aula[4] + '\n')


dicio('horarioss.txt', 'horario_novosss')