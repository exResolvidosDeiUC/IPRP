def nifsValidos(nifs):
    validos = {}
    for nif, nome in nifs.items():
        n = str(nif)
        if (9*int(n[0]) + 8*int(n[1]) + 7*int(n[2]) + 6*int(n[3]) + 5*int(n[4]) + 4*int(n[5]) + 3*int(n[6]) + 2*int(n[7]) + int(n[8])) % 11 == 0:
            validos.setdefault(nif, nome)
    return validos        