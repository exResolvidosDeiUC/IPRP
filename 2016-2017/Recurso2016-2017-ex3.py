lista_tuplos = [('2',1,1),('a',10,0),('x',0,0),('d',3,2),(' ',6,0),('c',7,0),('b',8,1)]

def decode(list):
    #ordenar tuplos por posicao do caracter
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j][1] > list[j+1][1]:
                list[j], list[j + 1] = list[j+1], list[j]
    string = ''
    for i in list:
        string += i[0]*(i[2]+1) #adicionar caracter repeticoes +1 vezes
    return string

print(decode(lista_tuplos))