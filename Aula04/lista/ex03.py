for i in range(4):
    salario = float(input('Insira o valor do salário bruto: \n'))
    inss = salario * 0.09
    print('O valor do inss do salario {:.2f} R$'.format(inss))
