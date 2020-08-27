operacao = int(input("Digite a operacao: 1-Adicao, 2-Subtracao, 3-Multiplicacao, 4-Divisao: "))

#Operacao invalida
if operacao < 1 and operacao > 4:
    print("Operacao Inválida")

#Adicao
if operacao == 1:
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    soma = num1 + num2
    print("O resultado da soma de ",num1," e ",num2," é igual a: ", soma)

#Subtracao
if operacao == 2:
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    subtracao = num1 - num2
    print("O resultado da subtracao de ",num1," e ",num2," é igual a: ", subtracao)

#Multiplicacao
if operacao == 3:
    num1 = float(input("Digite o valor do primeiro produto: "))
    num2 = float(input("Digite o valor do segundo produto: "))
    multiplicacao = num1 * num2
    print("O resultado da multiplicacao de ",num1," e ",num2," é igual a: ", multiplicacao)

#Divisao
if operacao == 4:
    dividendo = float(input("Digite o valor do dividendo: "))
    divisor = float(input("Digite o valor do divisor: "))
    if divisor == 0:
        print("Valor do divisor inválido")
    else:
        divisao = dividendo / divisor
        print("O resultado da divisao de ",dividendo," e ",divisor," é igual a: ", divisao)
