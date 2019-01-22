path = 'C:\\Users\\rilap\\Desktop\\ficheiros\\texto_palavras.txt'

def conta_ficheiro(nome_ficheiro):
    #abro o ficheiro e leio o que la esta guardando numa lista e fecho o ficheiro
    f = open(nome_ficheiro,'r')
    palavras = f.readlines()
    f.close()
 #crio um dicionario novo    
    dicio_count = dict()
    for i in range(len(palavras)):
        
        palavras[i]=palavras[i].split() 
#ciclo que percorre a lista usando o count que conta o numero de vezes que aquele elemento aparece na lista
        for j in range(len(palavras[i])):
            soma_count = 0
            soma_count+= palavras[i].count(palavras[i][j]) 
#as chaves sao os elementos da lista e os valores o count
            dicio_count[palavras[i][j]] = soma_count 
    return dicio_count
  
print(conta_ficheiro(path))