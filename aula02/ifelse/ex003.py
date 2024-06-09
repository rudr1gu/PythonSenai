senai = input('Qual unidade do senai? vila alpina ou mooca')
notaAluno = int(input('Insira a nota do aluno'))
presencaAluno = int(input('Insira a porcentacem de presença do aluno'))

if senai == 'vila alpina':
    if notaAluno >= 60 and presencaAluno >= 75:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
elif senai == 'mooca':
    if notaAluno >= 50 and presencaAluno >= 75:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
else:
    print('[ERRO] verifique o nome da unidade senai')

