time1 = str(input("Digite o nome do primeiro time: "))
golTime1 = int(input("Digite o numero de gols do primeiro time: "))
time2 = str(input("Digite o nome do segundo time: "))
golTime2 = int(input("Digite o numero de gols do segundo time: "))

if golTime1 > golTime2:
    print("O vencedor foi ",time1," com ",golTime1, "gols")
elif golTime2 > golTime1:
    print("O vencedor foi ",time2," com ",golTime2, "gols")
else:
    print("O jogo resultou em um EMPATE")



