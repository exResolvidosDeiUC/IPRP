def soma_valores(ficheiro, ficheiro_novo):
    with open(ficheiro, 'r') as file:
        dados = file.readlines()
    dados = [dado.replace('\n','') for dado in dados]
    dados = [i.split() for i in dados]
    dados_dict = {}
    for dado in dados:
        dados_dict.setdefault(dado[0], dado[1:])
        dados_dict[dado[0]].append(str(sum([int(i) for i in dado[1:]])))
    dados_temp = dados_dict.copy()
    dados_ord = {}
    for i in range(len(dados_dict)):
        for nome, vals in dados_dict.items():
            if len([j[-1] for j in dados_temp.values()]) > 0 and vals[-1] == max([j[-1] for j in dados_temp.values()]):
                dados_ord.setdefault(nome, vals)
                dados_temp.pop(nome)
    texto = ''
    for nome, vals in dados_ord.items():
        texto += nome + ' ' + ' '.join(vals) + '\n'
    with open(ficheiro_novo, 'w') as file:
        file.write(texto)