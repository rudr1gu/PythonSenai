notaAluno = input("Digite a nota do aluno de 0 a 100: ")

if int(notaAluno) >= 50:
    print('Aprovado')
elif int(notaAluno) > 100 or int(notaAluno) < 0:
    print('Nota inválida')
else:
    print('Reprovado')