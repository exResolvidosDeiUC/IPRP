def encontra_padroes(texto, padrao):
    pos = [0]
    for i in range(texto.count(padrao)):
        pos.append(texto.index(padrao, 0 if i == 0 else pos[-1] + 1)) 
    return pos

if __name__ == '__main__':
    print(encontra_padroes("Ola o meu nome é rebeca rebeca", "rebeca"))
