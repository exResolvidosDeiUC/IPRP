def colecao(ficheiro):
    with open(ficheiro, 'r') as file:
        bd = [linha.replace('\n', '') for linha in file.readlines()]
    bd = [linha.split(',') for linha in bd]
    amigos = []
    for linha in bd[1:]:
        if linha[2] != '' and linha[2] not in amigos:
            amigos.append(linha[2])
    return amigos        