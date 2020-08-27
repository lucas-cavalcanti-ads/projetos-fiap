def decrementaDias(data, qtd_dias):
    dia = data[0]
    mes = data[1]
    ano = data[2]

    acrescimo_dias  = qtd_dias
    x = 0

    while x < acrescimo_dias:
        dia -= 1
        if mes == 1 or mes ==3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia < 1:
                dia = 31
                mes -=1
                if mes < 1:
                    mes = 12
                    ano -=1
        elif mes == 2:
            if dia < 1:
                dia = 28
                mes -=1
                if mes < 1:
                    mes = 12
                    ano -=1
        elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia < 1:
                dia = 29
                mes -=1
                if mes < 1:
                    mes = 12
                    ano -=1
        else:
            if dia < 1:
                dia = 30
                mes -=1
                if mes < 1:
                    mes = 12
                    ano -= 1

        x +=1
    return (data,(dia,mes,ano))

d = (2,5,2019)
qtd = 365

retorno = decrementaDias(d,qtd)
tupla_data_inicial = retorno[0]
tupla_data_final = retorno[1]

print("A data  ",tupla_data_inicial[0],"/",tupla_data_inicial[1],"/",tupla_data_inicial[2]," - ", qtd, " dias é: ", tupla_data_final[0],"/",tupla_data_final[1],"/",tupla_data_final[2])

