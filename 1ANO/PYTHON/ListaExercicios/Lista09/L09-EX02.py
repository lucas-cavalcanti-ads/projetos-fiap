import random

def gerarNumeros(lista):

    return random.sample(lista, len(lista))

lista = [1,2,3,4,5,6,7,8]

listaAleatoria = gerarNumeros(lista)

print(listaAleatoria)