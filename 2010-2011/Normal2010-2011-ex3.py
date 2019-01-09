def retira_matriz(matriz, num):
    new_matriz = [[0] * len(matriz[0]) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            new_matriz[i][j] = matriz[i][j] - num if (matriz[i][j] - num) > 0 else 0
    return new_matriz

if __name__ == '__main__':
    matriz = [[5,15,0],[9,0,8]]
    print(retira_matriz(matriz, 6))