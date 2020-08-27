#item b
def contaDigitos(n,d):
    contador = 0

    while n != 0:
        dig  = n % 10
        if dig == d:
            contador += 1
        n =  n // 10
    return contador


a = 12345
b = 54321245



flag_conta = 9


permutacao = False

while flag_conta > 0:
    if contaDigitos(a, sflag_conta) != contaDigitos(b, flag_conta):
        permutacao = False
        
    else:
        permutacao = True
    flag_conta -= 1

if permutacao:
    print("é permutacao")
else:
    print("não é permutacao")