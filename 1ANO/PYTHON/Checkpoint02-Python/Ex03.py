def diferencaDias(data1, data2):
    # quantidade = (mes * 30) - (30 - dia)
    # suponto dia 5/10 > (10 * 30) - (30 - 5) = 300 - 25 = 275 dias
    qtd_dias_data1 = (data1[1] * 30) - (30 - data1[0]) #quantidade de dias do ano1 com o mes e dia
    qtd_dias_data2 = (data2[1] * 30) - (30 - data2[0]) #quantidade de dias do ano2 com o mes e dia

    #verificar quantos anos se passaram e multiplicar pela quantidade de dias por ano | 
    qtd_dias_ano = 365 * (data2[2] - data1[2])

    #total de dias = quantidade de dias com mes e ano do ano2 + quantida de dias pelos anos isso tudo menos a quantidade de dias com mes e ano do ano1
    total_dias = (qtd_dias_data2 + qtd_dias_ano) - qtd_dias_data1
    return "A diferenca entre os dias " + str(data1[0]) + "/" + str(data1[1]) + "/" + str(data1[2]) + " e " + str(data2[0]) + "/" + str(data2[1]) + "/" + str(data2[2]) + " é de " + str (total_dias) + " dias"

d1 = (27,10,1996)
d2 = (27,10,1998)

s = diferencaDias(d1,d2)

print(s)


