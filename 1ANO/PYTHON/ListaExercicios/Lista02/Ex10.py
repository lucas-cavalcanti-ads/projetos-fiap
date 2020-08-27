teclado = input("Digite o valor do primeiro salário: ")
salario1 = float(teclado)
teclado = input("Digite o valor segundo salário: ")
salario2 = float(teclado)

aumento = ((salario2 * 100) / salario1) - 100

print("O seu aumento de salario foi de ",aumento,"%")