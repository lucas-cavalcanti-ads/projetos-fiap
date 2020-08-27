idade = int(input("Nadador, escreve a sua idade para descobrir a sua categoria: "))
if idade < 5:
    print("Categoria: Nao definida")
elif idade >= 5 and idade <= 7:
    print("Categoria: Infantil")
elif idade >= 8 and idade <= 10:
    print("Categoria: Juvenil")
elif idade >= 11 and idade <= 15:
    print("Categoria: Adolecente")
elif idade >= 16 and idade <= 30:
    print("Categoria: Adulto")
elif idade >= 30:
    print("Categoria: Senior")