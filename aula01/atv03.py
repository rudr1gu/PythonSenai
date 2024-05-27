horasDia = 8
horasAulas = 80
porcentagemAceitavel = 0.25
limiteFaltas = (horasAulas / horasDia) * porcentagemAceitavel

faltas = int(input("Digite o numero de dias de faltas do aluno: "))
nota = float(input("Digite a nota do aluno: "))

if faltas <= limiteFaltas:
    if nota < 0 or nota > 100:
        print("Nota inválida.")
    elif nota >= 60:
        print("Aluno aprovado!")
        if nota == 100:
            print("Parabens nota maxima!")
    elif nota >= 30:
        print("Aluno em recuperação.")    
    else:
        print("Aluno reprovado devido à nota.")
else:
    print("Aluno reprovado devido ao número de faltas.")
