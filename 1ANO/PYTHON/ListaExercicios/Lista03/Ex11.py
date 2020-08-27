produto = float(input("Digite o valor da etiqueta do produto(R$): "))
tipoPagamento = int(input("Seleciona a forma de pagamento:1-Débito, 2-Crédito, 3-Cheque, 4-Dinheiro: "))
if tipoPagamento < 1 and tipoPagamento > 4:
    print("Forma de pagamento invalida")
elif tipoPagamento == 1 or tipoPagamento == 3 or tipoPagamento == 4:
    valorFinal = produto - (produto * 0.1)
    print("Valor final do produto com desconto de 10%: R$",valorFinal)
else:
    quantidade = int(input("Digite 1 para pagamento a vista no credito, 2 para parcelar em 2X, 4 para parcelar em 4X: "))
    if quantidade == 1:
        valorFinal = produto - (produto * 0.05)
        print("Valor final do produto com desconto de 5%: R$",valorFinal)
    elif quantidade == 2:
        valorFinal = produto
        valorParcela = valorFinal / 2
        print("Valor final do produto: R$",valorFinal," em 2X de R$",valorParcela)
    elif quantidade == 4:
        valorFinal = produto * 1.07
        valorParcela = valorFinal / 4
        print("Valor final do produto: R$",valorFinal," em 4X de R$",valorParcela)
    else:
        print("Valor de parcela invalido")
    
