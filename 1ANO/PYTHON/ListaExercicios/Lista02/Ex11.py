teclado = input("Digite o seu RM(5 numeros): ")
rm = int(teclado)

num1 = rm % 10
num2 = num1 % 10
num3 = num2 % 10
num4 = num3 % 10
num5 = num4 % 10

resultado = num1 + num2 + num3 + num4 + num5
print(resultado)