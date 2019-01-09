def soma_vet(v1,v2):
    soma = v1.copy()
    for k,v in v2.items():
        soma.setdefault(k, 0)
        if k != 'len':
            soma[k] += v 
    return soma    

def soma_file(ficheiro):
    with open(ficheiro, 'r') as file:
        vets = [i.replace('\n','') for i in file.readlines()]
        vets = [i.split(',') for i in vets]        
    esparsos = []
    for vet in vets:
        dict_temp = {}
        for i in range(len(vet)):
            if int(vet[i]) != 0:
                dict_temp.setdefault(i, int(vet[i]))
        dict_temp['len'] = len(vet)
        esparsos.append(dict_temp)
    print(esparsos)
    vet_soma = {'len':len(vets[0])}
    for esparso in esparsos:
        vet_soma = soma_vet(vet_soma, esparso)
    return vet_soma    