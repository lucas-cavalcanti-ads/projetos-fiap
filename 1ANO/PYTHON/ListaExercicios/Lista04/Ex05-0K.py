flagNumero = 0

num = int(input("Digite um numero: "))
flagNumero = num

while flagNumero > 0:

    if num % flagNumero == 0:
        print("Numero divisivel: ", flagNumero)
    
    flagNumero -= 1

