def users_dei(dicio, ficheiro):
    with open(ficheiro, 'r') as file:
        users = [linha.replace('\n','')[linha.replace('\n','').index('~') + 1:] for linha in file.readlines()]
    nomes = list(filter(None, [dicio[user][0] if user in dicio else None for user in users]))
    nomes.sort()
    return nomes



if __name__ == '__main__':
    dictio = {}
    ficheiro = ''
    print(users_dei(dictio, ficheiro))