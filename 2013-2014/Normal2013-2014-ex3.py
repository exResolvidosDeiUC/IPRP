receitas = {
'sonhos':['agua', 'farinha', 'manteiga', 'ovos', 'acucar'], 'rabanadas':['pao', 'leite', 'ovos', 'manteiga', 'acucar'], 'leite creme':['acucar', 'farinha', 'ovos', 'leite']}

def ingredientes_mais_usados(receitas):
    # criação de uma lista com os ingredientes sem repetições
    sem_rep = []
    for j in receitas:
        for i in receitas[j]:
            if i not in sem_rep:
                sem_rep.append(i)
    #print(sem_rep)

    # criação de uma lista com os ingredientes mais usados
    mais = []
    for l in sem_rep:
        cont = 0
        for j in receitas:
            if l in receitas[j]:
                cont += 1
        if cont == len(receitas):
            mais.append(l)
    #print(mais)

    # criação do dicionário
    final = {}
    for ingrediente in mais: #percorre lista de ingredientes mais usados
        for x, y in receitas.items(): #percorre dicionario de receitas, x é receita, y é lista de ingredientes de receita x
            if ingrediente in y: #se ingrediente do primeiro ciclo existe na lista de ingredientes y
                if final.get(ingrediente) is not None: #verifica se este ingrediente já existe no dicionario final
                    final[ingrediente].append(x) #em caso afirmativo, acrescenta a receita x
                else:
                    final[ingrediente] = [x] #em caso negativo cria essa entrada no dicionário, sendo que o valor é uma lista com essa receita apenas
    #print(final)

    return final


ingredientes_mais_usados(receitas)