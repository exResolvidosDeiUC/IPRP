def produto_escalar(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

print(produto_escalar((1, 2, 3), (0, 1, 2)))
