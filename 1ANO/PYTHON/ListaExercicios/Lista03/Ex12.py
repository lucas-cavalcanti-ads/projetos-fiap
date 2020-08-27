print("Olá, bem vindo ao programa de médias semestrais!")
media1 = float(input("Digite a nota do primeiro semestre: "))
media2 = float(input("Digite a nota do segundo semestre: "))
nAulas = int(input("Digite o total de aulas letivas: "))
nAulasAssistidas = int(input("Digite o numero de aulas assistidas: "))


#Calcular a media final do aluno 1Sem 40% / 2Sem 60%
mediaFinal = (media1 * 0.4) + (media2 * 0.6)

#Calcular se o aluno tem mais de 70% de frequencia;
# < 70% = Reprovado 
int minFrequencia = (nAulas * 0.7)
if nAulasAssistidas < minFrequencia:
    print("Voce está REPROVADO")
else: # < 4 = Reprovado; >= 4 & < 6 = Exame; >= 6 = Aprovado;
    if mediaFinal < 4:
      print("Voce está REPROVADO")
    elif mediaFinal >= 4 & mediaFinal < 6:
        print("Aluno em EXAME")
    else:
        print("Aluno APROVADO") 





