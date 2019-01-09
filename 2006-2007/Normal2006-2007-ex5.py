def produto_escalar(v1, v2):
    soma = 0
    for i in range(len(v1)):
        soma += v1[i] * v2[i]
    return soma
    #abaixo, solução em 1 só linha
    #return sum(v1[i] * v2[i] for i in range(len(v1)))

print(produto_escalar((1, 2, 3), (0, 1, 2)))
