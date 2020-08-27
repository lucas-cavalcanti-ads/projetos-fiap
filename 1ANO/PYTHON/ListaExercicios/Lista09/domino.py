import random

#funcao que mistura as pedras
def misturaPedras(pedras):
    #Esse é um jeito de misturar
    # x = 0
    # while x < 100:
    #     i = random.randint(0, 27)
    #     j = random.randint(0, 27)
    #     aux = pedras[j]
    #     pedras[j] = pedras[i]
    #     pedras[i = aux]
    #     x +=1

    #Esse é outro jeito de misturar
    return random.sample(pedras, len(pedras))

#função que cria o domino
def criarDomino():
    domino = []
    j = 0
    #Criando as 7 pedras
    while j < 7:
        i = j
        #Adicionando valores as pedras
        while i < 7:
            domino.append([j,i])
            i += 1
        j += 1

    #Misturando as pedras
    pedrasMisturadas = misturaPedras(domino)
    
    return pedrasMisturadas

#funcão que distribui as pessoas
def distribuiPedras(pedras, qtd):
    mao = []
    while qtd > 0:
        mao.append(pedras.pop(0)) 
        qtd-=1
    return mao
def jogadaHomem(mao, domino):
    for x in range(0, len(mao)):
        posicaoPedra = x + 1
        print("Pedra",posicaoPedra,mao[x])
    posicao = int(input("Digite a posição da pedra que deseja jogar: "))
    while posicao == -1:
        mao.append(domino.pop())
        for x in range(0, len(mao)):
            posicaoPedra = x + 1
            print("Pedra",posicaoPedra,mao[x])
        posicao = int(input("Digite novamente uma posição: "))

    return mao.pop(posicao - 1)

def jogadaCpu(mao, domino, esquerda, direita):
    i = 0
    while i < len(mao):
        pedra = mao[i]
        if pedra[0] == esquerda or pedra[1] == esquerda:
            return mao.pop(i)
        if pedra[0] == direita or pedra[1] == direita:
            return mao.pop(i)
        i = i + 1
        if i == len(mao):
            mao.append(domino.pop())

mesa = []
pedras = criarDomino()
maoHomem = distribuiPedras(pedras, 7)
maoMaquina = distribuiPedras(pedras, 7)

#mesa vazia
pedra = jogadaHomem(maoHomem, pedras)
mesa.append(pedra)
direita = pedra[1]
esquerda = pedra[0]
print("Mesa: ",mesa)
i = 1
while len(maoHomem) > 0 or len(maoMaquina) > 0:
    if i % 2 == 1:
        pedra = jogadaCpu(maoMaquina, pedras, esquerda, direita)
    else:
        pedra = jogadaHomem(maoHomem, pedras)
    i+=1
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
        print("JOGADA INVALIDA")        

    print("Mesa: ",mesa)

else:
    print("Voce está sem pedras")

# print("Homem: ",maoHomem)
# print("Maquina: ",maoMaquina)
        
