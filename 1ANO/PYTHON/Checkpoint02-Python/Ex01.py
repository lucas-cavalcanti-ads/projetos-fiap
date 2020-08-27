def acrescentaDias(data, qtd_dias):
    dia = data[0]
    mes = data[1]
    ano = data[2]

    acrescimo_dias  = qtd_dias

    x = 0

    while x < acrescimo_dias:

        dia += 1

        if mes == 1 or mes ==3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 31:
                dia = 1
                mes += 1
                if mes > 12:
                    mes = 1
                    ano += 1
        elif mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                if dia > 29:
                    dia = 1
                    mes += 1
                    if mes > 12:
                        mes = 1
                        ano += 1
            elif dia > 28:
                dia = 1
                mes += 1
                if mes > 12:
                    mes = 1
                    ano += 1
        
        else:
            if dia > 30:
                dia = 1
                mes += 1
                if mes > 12:
                    mes = 1
                    ano += 1

        x += 1
    return (data,(dia,mes,ano))

d = (28,2,2019)
qtd = 367

retorno = acrescentaDias(d,qtd)
tupla_data_inicial = retorno[0]
tupla_data_final = retorno[1]

print("A data  ",tupla_data_inicial[0],"/",tupla_data_inicial[1],"/",tupla_data_inicial[2]," + ", qtd, " dias é: ", tupla_data_final[0],"/",tupla_data_final[1],"/",tupla_data_final[2])
