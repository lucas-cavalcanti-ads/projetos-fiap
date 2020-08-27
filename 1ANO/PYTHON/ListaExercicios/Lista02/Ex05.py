pi = 3.141592
teclado = input("Informe o raio do circulo: ")
raio = float(teclado)
#Calculo Perimetro > Perimetro = 2pi.r
perimetro = (2 * pi) * raio
perimetror = str(perimetro)
#Calculo da Area > pi.rquadrado
area = pi * (raio ** 2)
arear = str(area)

print("O valor do perimetro e: " + perimetror)
print("O valor da area e: " + arear)