def numerosIguais(listaA, listaB):
    numerosIguais = []
    qtdListaA = len(listaA)
    qtdListaB = len(listaB)
    i=0

    if len(listaA) >= len(listaB):        
        while i < qtdListaB:
            x=0
            numero = listaB[i]
            while x < qtdListaA:
                if numero == listaA[x]:
                    numerosIguais.append(listaA[x])
                x+=1
            i+=1
    else:
        while i < qtdListaA:
            x=0
            numero = listaA[i]
            while x < qtdListaB:
                if numero == listaB[x]:
                    numerosIguais.append(listaB[x])
                x+=1
            i+=1
    return numerosIguais

vetA = [1, 6, 10, 24, 25, 30, 45]
vetB = [1, 3, 10, 12, 25, 15, 45]
numerosIguais = numerosIguais(vetA, vetB)

print("Os numeros da lista A sao: ", vetA)
print("Os numeros da lista B sao: ", vetB)
print("Os numeros iguais sao: ", numerosIguais)
