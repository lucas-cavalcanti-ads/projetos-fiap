teclado = input("Digite o valor do prduto (R$): ")
produto = float(teclado)
teclado = input("Digite o valor do desconto (%): ")
desconto = float(teclado)

valorDesconto = produto - (produto * (desconto / 100))

print("O valor com desconto é: R$",valorDesconto,)
