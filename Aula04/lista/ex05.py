nomes = ['Luffy', 'Sandy', 'Nami', 'Zoro', 'Naruto', 'Shikamaru', 'Goku']

for i in range(2):
    nome = input('Insira um nome: \n')
    nomes.append(nome)

for i in nomes:
    print('Bom dia {}! bem vindo ao nosso encontro'.format(i))
