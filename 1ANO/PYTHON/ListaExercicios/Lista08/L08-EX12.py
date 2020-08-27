def numeroOcorrencia(lista):
    qtdLista = len(lista)
    i = 0

    listaLetras = []
    listaLetras.append(lista[0])
    print(len(listaLetras))
    while i < qtdLista:
        #print("ENTROU NO PRIMEIRO WHILE")
        qtdListaLetras = len(listaLetras)
        x = 0
        while x < qtdListaLetras:
            #print("ENTROU NO SEGUNDO WHILE")
            if listaLetras[x] == lista[i]: 
               print("")
            else:
                listaLetras.append(lista[i])
            x+=1
        i+=1
    #qtdA = lista.count('a')
    

    return listaLetras
    


listaLetras = ['a', 'a', 'b', 'a', 'c', 'a', 'b', 'a', 'e', ]

print(numeroOcorrencia(listaLetras))



