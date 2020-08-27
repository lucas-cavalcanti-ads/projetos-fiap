def adicionarEspacos(palavra, letra):
    qtd_letras = len(palavra)
    if palavra[1] == letra:
        
        nova_palavra = palavra.replace(palavra[0], '*')
    
    return nova_palavra, qtd_letras

palavra = str(input("Digite uma palavra: "))
letra = str(input("Digite uma letra: "))

print(adicionarEspacos(palavra, letra))