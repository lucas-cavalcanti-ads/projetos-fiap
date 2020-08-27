import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = ((b * b) - ((4 * a) * c))
if delta < 0:
    delta = delta * -1
rdelta = math.sqrt(delta)
x1 = ((b * -1) + rdelta) / (2 * a)
x2 = ((b * -1) - rdelta) / (2 * a)

print("Coeficientes:a -",a,",b -",b,",c -",c)
print("Resultados:x1- ",x1,", x2- ",x2)