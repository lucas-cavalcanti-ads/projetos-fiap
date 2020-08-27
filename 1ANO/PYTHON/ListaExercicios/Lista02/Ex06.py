teclado = input("Digite um numero: ")
num = int(teclado)

dezena = num / 10
dezenai = int(dezena)
dezenar = str(dezenai)
unidade = int(num % 10)
unidader = str(unidade)

print("O numero da dezena é:{}".format(dezenar))
print("O numero da unidade é: " + unidader)

