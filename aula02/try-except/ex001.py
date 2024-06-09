salario =  input('Digite o salário: ').strip().replace(',','.').replace('R$','').replace(' ','').replace('.','')

try:
    salario = float(salario)
    salarioAnual = salario*12

    if salarioAnual < 22847:
        taxa = 0
    elif salarioAnual < 33919:
        taxa = 0.075
    elif salarioAnual < 45012:
        taxa = 0.15
    elif salarioAnual < 55976:
        taxa = 0.225
    else:
        taxa = 0.275
    
    imposto = salarioAnual*taxa
    print(f'Salário anual: R${salarioAnual:.2f}')
    print(f'Taxa: {taxa*100:.1f}%')
    print(f'Imposto: R${imposto:.2f}')
   
except ValueError:
    print('Salário inválido')
except:
    print('Erro desconhecido')
