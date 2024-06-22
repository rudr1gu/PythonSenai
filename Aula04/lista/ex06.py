nomes = []
salarios = []


for i in range(5):
    nome = input('Insira o seu nome: \n')
    nomes.append(nome)
    salario = float(input('Insira o valor do seu salario'))
    salarios.append(salario)

for a in range(5):
    print('{} o valor do seu inss é de {:.2f} R$'.format(nomes[a], salarios[a] * 0.09))
