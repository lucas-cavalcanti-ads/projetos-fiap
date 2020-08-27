def adicionarEspacos(palavra):
    espaco = 0
    qtd_letras = len(palavra)
    nova_palavra = palavra[espaco] + " "
    espaco += 2
    nova_palavra = palavra[espaco] + " "
    espaco += 2
    nova_palavra = palavra[espaco] + " "

    return nova_palavra, qtd_letras

palavra = str(input("Digite uma palavra: "))

print(adicionarEspacos(palavra))