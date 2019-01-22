dicio = {'esta':['es','ta'],'linha':['li','nha'],'parece':['pa','re','ce'],'demasiado':['de','ma','si','a','do'],'longa':['lon','ga'],'e':['e'],'vai':['vai'],'aos':['aos'],'bocados':['bo','ca','dos'],'de':['de'],'ser':['ser'],'dividida':['di','vi','di','da']}
string = 'esta linha parece demasiado longa e vai ser dividida aos bocados'

def hifenar(frase, n, dic):
    frase = frase.split() #dividir palavras a ser trabalhadas individualmente
    linhas = [''] #criar lista com novas linhas do texto
    j = 0 #indice da linha a ser criada
    for i in frase: #i é uma palavra da frase
        for divisao in dic[i]: #percorre divisoes dessa palavra
            if len(linhas[j]) + len(divisao) >= n: #divisao nao cabe
                if linhas[j][-1] != ' ': #está a meio de uma palavra
                    linhas[j] += '-' #adiciona hifen
                j+=1 #muda de linha
                linhas.append('') #cria nova linha vazia na lista de linhas
            linhas[j] += divisao #acrescenta proxima divisao da palavra
        linhas[j] += ' ' #acabou palavra logo adiciona espaço
    string = ''
    for i in linhas: #adiciona diversas linhas a uma so string, acrescentado \n para representar mudancas de linhas
        string+= i + '\n'
    return string

print(hifenar(string, 21, dicio))