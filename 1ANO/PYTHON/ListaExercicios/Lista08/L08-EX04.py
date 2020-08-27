n = int(input("Escreva um número: "))
qtdNumeros = int(input("Escreva a quantidade de numeros que quer somar: "))
i = 0
v = []
while i < qtdNumeros:
    numero = float(input("Digite um numero qualquer: "))
    v.append(numero)    
    i+=1

qtdLista = len(v)
x = 0
while x < qtdLista:
    valor = v[x] + v[n-(x+1)]
    print(valor)
    x+=1

#v[0] + v[n − 1]
# v[1] + v[n − 2]
# v[2] + v[n − 3]

