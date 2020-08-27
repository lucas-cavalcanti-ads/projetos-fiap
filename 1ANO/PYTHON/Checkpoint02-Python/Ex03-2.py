def calculaDias(data1, data2):
    dia1 = data1[0]
    mes1 = data1[1]
    ano1 = data1[2]

    dia2 = data2[0]
    mes2 = data2[1]
    ano2 = data2[2]

    qtd_dias = 0

    while dia1 != dia2 or mes1 != mes2 or ano1 != ano2:
        
        qtd_dias += 1

        dia1 += 1

        if mes1 == 1 or mes1 ==3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12:
            if dia1 > 31:
                dia1 = 1
                mes1 += 1
                if mes1 > 12:
                    mes1 = 1
                    ano1 += 1
        elif mes1 == 2:
            if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
                if dia1 > 29:
                    dia1 = 1
                    mes1 += 1
                    if mes1 > 12:
                        mes1 = 1
                        ano1 += 1
            elif dia1 > 28:
                dia1 = 1
                mes1 += 1
                if mes1 > 12:
                    mes1 = 1
                    ano1 += 1
        
        else:
            if dia1 > 30:
                dia1 = 1
                mes1 += 1
                if mes1 > 12:
                    mes1 = 1
                    ano1 += 1
    return (qtd_dias)

d1 = (5,3,2019)
d2 = (5,3,2020)

qtd = calculaDias(d1,d2)

print(qtd)

