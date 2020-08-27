num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
resto = num1 % num2

if resto == 0:
    print(num1," é divisivel por ",num2)
else: print(num1," nao é divisivel por ",num2)