def verificarNumeros(x, lista):
    qtdMaior = 0
    numerosMaiores = []
    qtdLista = len(lista)
    i=0

    while i < qtdLista:
        if lista[i] >= x:
            qtdMaior+=1
            numerosMaiores.append(lista[i])
        i+=1
    
    return [qtdMaior, numerosMaiores]

numero = float(input("Escreva um número: "))
vet = [1, 6, 10, 24, 25, 30, 45]
resultado = verificarNumeros(numero,vet)
qtdMaior = resultado[0]
numerosMaiores = resultado[1]

print("Quantidade de numeros maiores ou iguais: ",qtdMaior)
print("Os numeros maiores que ", numero, ", sao: ", numerosMaiores)