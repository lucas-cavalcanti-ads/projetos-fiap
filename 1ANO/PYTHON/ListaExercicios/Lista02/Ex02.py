teclado = input("Escreva seu nome: ")
nome = str(teclado)
teclado = input("Escreva seu sobrenome: ")
sobrenome = str(teclado)
teclado = input("Digite o seu ano de nascimento: ")
anoNasc = int(teclado)

idade = 2020 - anoNasc

idadeNascimento = str(idade)

print("O seu nome é " + nome + " " + sobrenome + " e voce tem " + idadeNascimento + " anos")

