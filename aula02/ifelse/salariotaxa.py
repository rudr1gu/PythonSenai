salario = int(input('Informe o valor do seu salario: '))
salarioAnual = salario * 12

if salarioAnual < 22847:
    taxa = 0
elif salarioAnual< 33919:
    taxa = .07
elif salarioAnual < 45012:
    taxa = .15
elif salarioAnual < 55976:
    taxa = .225
else:
    taxa = .275

print('A o valor da taxa é {:.2f}% e seu salario anual é {}'.format(taxa*100, salarioAnual))
print('O imposto anual do seu salario será de: {:.2f}R$'.format(salarioAnual * taxa))