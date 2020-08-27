import random


def gerarNumeros(numero):
    i = 0
    listaNumeros = []
    while i < numero:
        numeroAleatorio = random.randint(1,1001)
        listaNumeros.append(numeroAleatorio)
        i+=1
    return listaNumeros
    

numero = int(input("Escreva um número: "))
listaNumeros = gerarNumeros(numero)
print(listaNumeros)