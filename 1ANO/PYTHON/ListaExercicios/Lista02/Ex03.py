teclado = input("Digite o primeiro numero: ")
num1 = int(teclado)
teclado = input("Digite o segundo numero: ")
num2 = int(teclado)

soma = num1 + num2
somar = str(soma)
subtracao = num1 - num2
subtracaor = str(subtracao)
multiplicacao = num1 * num2
multiplicacaor = str(multiplicacao)
divisao = num1 / num2
divisaor = str(divisao)
resto = num1 % num2
restor = str(resto)

numero1 = str(num1)
numero2 = str(num2)

print("A soma de " + numero1 + " + " + numero2 + " e igual a: " + somar)
print("A soma de " + numero1 + " + " + numero2 + " e igual a: " + subtracaor)
print("A multiplicacao de " + numero1 + " + " + numero2 + " e igual a: " + multiplicacaor)
print("A divisao de " + numero1 + " + " + numero2 + " e igual a: " + divisaor)
print("O resto de " + numero1 + " + " + numero2 + " e igual a: " + restor)