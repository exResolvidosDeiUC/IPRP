def decode(seq):
    seq = [i.split(']') for i in seq.split('[')]
    texto = ''; num = ''
    for i in seq:
        for j in i:
            for car in j:
                if car.isdigit():
                    num += car
                elif car.isalpha() and num != '':
                    texto += car * int(num)
                    num = ''
                else:
                    texto += car
    return texto

if __name__ == '__main__':
    print(decode("AB[12c]d[2E][4F]g"))