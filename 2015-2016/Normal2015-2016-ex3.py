def conta(cad, sub_cad):
    cnt = 0
    for i in range(len(cad)-len(sub_cad)+1):
        if cad[i:i+len(sub_cad)] == sub_cad:
            cnt+=1
    return cnt
print(conta('olalal mundo', 'lal'))
