i = 0
listaPalavras = []

while i < 10:
    palavra = str(input("Escreva uma palavra: "))
    listaPalavras.append(palavra)
    i+=1

x = 0
quantidadeItensLista = len(listaPalavras)
qtd = quantidadeItensLista - 1
listaInvertida = []
while x < quantidadeItensLista:
    
    listaInvertida.append(listaPalavras[qtd])
    qtd -=1
    x+=1

print(listaPalavras)
print(listaInvertida)
