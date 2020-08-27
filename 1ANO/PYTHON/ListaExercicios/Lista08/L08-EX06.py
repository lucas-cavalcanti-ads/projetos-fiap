def insereOrdenado(x, lista):
    qtdLista = len(lista)
    i=0
    while i < qtdLista:
        if x < lista[i]:
            lista.insert(i,x)
            return lista
        i+=1
    

vet = [1, 6, 10, 24, 25, 30, 45] 
novaLista = insereOrdenado(44, vet)
print(novaLista)