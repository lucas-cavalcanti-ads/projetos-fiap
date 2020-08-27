def verificaOrdem(lista):
    i = 0
    qtdLista = len(lista)
    while i < qtdLista:
        
        numeroAtual = lista[i]
        numeroAnterior = lista[i-1]

        if i == 0:
            #nao faca nada
            print("Essa lista está: ")
        elif numeroAtual < numeroAnterior:
            return False
        i+=1

    return True
    
listaNumero = [1,2,3]
ordenado = verificaOrdem(listaNumero)
if(ordenado):
    mensagem = "ORDENADA"
else:
    mensagem = "DESORDENADA"
print(mensagem)

