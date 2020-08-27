notaFinal = 0
numAlunos = int(input("Digite a quantidade de alunos: "))
flagNumAlunos = numAlunos
contMaior = 0

while numAlunos > 0:
    nota = int(input("Digite a nota do aluno: "))
    if nota > 3:
        contMaior += 1
    notaFinal = notaFinal + nota
    numAlunos -= 1

contMenor = flagNumAlunos - contMaior
media = notaFinal / flagNumAlunos
print("A media de nota dos ", flagNumAlunos," alunos é: ", media)
print("Dos ", flagNumAlunos," alunos, ",contMaior, "ficaram com nota maior que 5 e ", contMenor, " ficaram com nota menor que 5")
