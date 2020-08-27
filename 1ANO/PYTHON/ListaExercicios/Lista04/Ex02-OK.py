notaFinal = 0
numAlunos = int(input("Digite a quantidade de alunos: "))
flagNumAlunos = numAlunos

while numAlunos > 0:
    nota = int(input("Digite a nota do aluno: "))
    notaFinal = notaFinal + nota
    numAlunos -= 1

media = notaFinal / flagNumAlunos
print("A media de nota dos ", flagNumAlunos," alunos é: ", media)
