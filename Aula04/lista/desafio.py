nomes = []
salarios = []

for i in range(5):
    nome = input('Insira o seu nome: \n')
    salario = float(input('Insira o valor do seu salario'))
    try:
        salarios.append(salario)
        nomes.append(nome)
    except:
        print('Digite um valor valido somente numeros')


for a in range(len(nomes)):
    if salarios[a] <= 1412:
        print('{} o valor do seu inss é de {:.2f} R$'.format(nomes[a], salarios[a] * 0.075))
    elif salarios[a] <= 2666:
        print('{} o valor do seu inss é de {:.2f} R$'.format(nomes[a], salarios[a] * 0.09))
    elif salarios[a] <= 4000:
        print('{} o valor do seu inss é de {:.2f} R$'.format(nomes[a], salarios[a] * 0.12))
    elif salarios[a] <= 7786:
        print('{} o valor do seu inss é de {:.2f} R$'.format(nomes[a], salarios[a] * 0.14))
    else:
        print('{} o valor do seu inss é de {:.2f} R$'.format(nomes[a], 7786 * 0.14))