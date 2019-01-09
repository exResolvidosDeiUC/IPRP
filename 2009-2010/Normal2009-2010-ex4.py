def fich_dic(ficheiro):
    with open(ficheiro, 'r') as file:
        pals = ["".join([j if j.isalpha() else '' for j in i]) for i in file.read().replace('\n',' ').split()]
    unicas = []
    for pal in pals:
        if pal not in unicas:
            unicas.append(pal)
    dicti = {}
    for pal in unicas:
        dicti.setdefault(len(pal), [])
        dicti[len(pal)].append(pal)
    return dicti

if __name__ == '__main__':
    ficheiro = ''
    print(fich_dic(ficheiro))