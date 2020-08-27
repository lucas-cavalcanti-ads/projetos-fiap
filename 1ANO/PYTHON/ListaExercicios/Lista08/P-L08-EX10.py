def intercala(listaA, listaB):
    print("Entrou na funcao")

    novaLista = []
    qtdListaA = len(listaA)
    qtdListaB = len(listaB)
    i=0
    
    #intercalando listaA
    while i < qtdListaA:
        novaLista.append(listaA[i])
        i+=1
    
    x=0

    #intercalando listaB
    while x < qtdListaB:
        qtdNovaLista = len(novaLista)
        numeroB = listaB[x]
        y=0

        while y < qtdNovaLista:
            if numeroB < novaLista[y]:
                if numeroB == novaLista[y]:
                    print("")
                else:
                    novaLista.insert(y,numeroB)

            y+=1

        x+=1

    i=0

    
       i+=1 

    return novaLista


    
vetA = [1, 6, 10, 11, 45]
vetB = [2, 3, 12]
numerosIntercalados = intercala(vetA, vetB)

print("Os numeros da lista A sao: ", vetA)
print("Os numeros da lista B sao: ", vetB)
print("Os numeros iguais sao: ", numerosIntercalados)