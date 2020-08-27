from datetime import date
print("Bem vindo ao programa de informacao de datas")
hoje = date.today()
print("Voce está executando esse programa em:",hoje.day,"/",hoje.month,"/",hoje.year)
dia = int(input("Digite o dia de hoje(Ex:22, 09): "))
mes = int(input("Digite o mes de hoje(Ex:07, 12): "))
ano = int(input("Digite o ano de hoje(Ex:2016, 2020): "))

if mes == 2:
    if dia > 28 or dia < 1:
        print("Formato de data inválido")
    elif (dia > 31 or dia < 1) or (mes < 1 or mes > 12):
        print("Formato de data inválido")
    else:
        print("Data digitada:",dia,"/",mes,"/",ano)
