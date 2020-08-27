#item a
def contaDigitos(n,d):
    contador = 0

    while n != 0:
        dig  = n % 10
        if dig == d:
            contador += 1
        n =  n // 10
    return contador

