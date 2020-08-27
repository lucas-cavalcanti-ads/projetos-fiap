import random

def criaDomino():
    domino = []
    j = 0
    while j < 7:
        i = j
        while i < 7:
            domino.append([j, i])
            i = i + 1
        j = j + 1    
    return domino

def mistura(domino):
    for contagem in range(1, 100):
        i = random.randint(0, 27)
        j = random.randint(0, 27)
        aux = domino[j]
        domino[j] = domino[i]
        domino[i] = aux

def distribui(domino, qtd):
    mao = []
    while qtd > 0:
        mao.append(domino.pop(0))
        qtd = qtd - 1

    return mao

def jogadaHomem(mao, domino):
    print("Mao", mao)
    pos = int(input("Informe a posicao que deseja jogar: "))
    while pos == -1:
        mao.append(domino.pop())
        print("Mao", mao)
        pos = int(input("Informe a posicao que deseja jogar: "))

    return mao.pop(pos)

def jogadaCpu(mao, domino, esq, dir):
    i = 0
    while i < len(mao):
        pedra = mao[i]
        if pedra[0] == esq or pedra[1] == esq:
            return mao.pop(i)
        if pedra[0] == dir or pedra[1] == dir:
            return mao.pop(i)
        i = i + 1
        if i == len(mao):
            mao.append(domino.pop())

mesa = []
pedras = criaDomino()
mistura(pedras)
homem = distribui(pedras, 7)
maquina = distribui(pedras, 7)

#mesa vazia
pedra = jogadaHomem(homem, pedras)
mesa.append(pedra)
direita = pedra[1]
esquerda = pedra[0]
print("Mesa ", mesa)
i = 1
while len(homem) > 0 or len(maquina) > 0:
    if i % 2 == 1:
        pedra = jogadaCpu(maquina, pedras, esquerda, direita)
    else:    
        pedra = jogadaHomem(homem, pedras)    
    
    i = i + 1

    if pedra[0] == esquerda:
        mesa.insert(0, pedra)
        esquerda = pedra[1]
    elif pedra[1] == esquerda:
        mesa.insert(0, pedra)
        esquerda = pedra[0]
    elif pedra[0] == direita:
        mesa.append(pedra)
        direita = pedra[1]
    elif pedra[1] == direita:
        mesa.append(pedra)
        direita = pedra[0]            
    else:
        print("Jogada invalida")

    print("Mesa ", mesa)
