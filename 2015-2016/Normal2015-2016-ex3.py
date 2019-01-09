def conta(cad, sub_cad):
    cnt = 0
    for i in range(len(cad)-len(sub_cad)+1): #numero de sub-cadeias a ser testadas
        if cad[i:i+len(sub_cad)] == sub_cad: #fatiamento da dimensão de sub_cad
            cnt+=1 #encontrando uma ocorrência, incrementa
    return cnt
print(conta('olalal mundo', 'lal'))
