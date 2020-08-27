positivo = 0
negativo = 0
soma = 0

quantidade = int(input("Digite a quantidade de numeros que deseja somar: "))

while quantidade > 0:
    num = int(input("Digite um valor: "))
    if num > 0:
        positivo += 1
    else: negativo += 1

    soma += num
    quantidade -= 1
    

print("Positivos: ",positivo," / Negativo: ", negativo)
print("A soma dos valores é de: ",soma)


