def numerosPares(lista):
    numerosPares = []
    qtdLista = len(lista)
    i=0

    while i < qtdLista:
        if lista[i] % 2 == 0:
            numerosPares.append(lista[i])
        i+=1
    
    return numerosPares

vet = [1, 6, 10, 24, 25, 30, 45]
numerosPares = numerosPares(vet)

print("Os numeros pares sao: ", numerosPares)
