# for i in range(10):
#     print('bom dia')

nomes = []

for i in range(5):
    nome = input('Insira um nome: \n')
    nomes.append(nome)

for i in nomes:
    print('Bom dia {}'.format(i))