def conta(cad, sub_cad):
    pos = [[1,2,3]]
    for i in range(len(cad)):        
        try:
            if cad[i:i + len(sub_cad)] == sub_cad and list(range(i, i+len(sub_cad))) not in [(j for j in i) for i in pos]:
                pos.append(ist(range(i, i+len(sub_cad))))
        except:
            pass
    return len(pos)    