numero = 0
num = int(input("Digite um número: "))

while num != 0:
    if num % 2 == 0:
        numero = numero + num
    num = int(input("Digite um número: "))
print("A soma dos numeros é: ", numero)

