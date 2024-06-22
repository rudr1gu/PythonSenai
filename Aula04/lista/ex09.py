def consultar():
    for i in range(len(carros)):
        print('Produto: {}, Valor {:.2f}'.format(carros[i], valores[i]))

def removerCarros():
    carro = input('digite o nome do carro que você deseja excluir: \n')

    if carro in carros:
        indice = carros.index(carro)
        carros.remove(carro)
        valores.pop(indice)

        for i in range(len(carros)):
            print('Produto: {}, Valor {:.2f}'.format(carros[i], valores[i]))

def adicionarCarro():
    carro = input('Digite o nome do carro: \n')
    valor = input('Digite o valor do carro: \n')
    carros.append(carro)
    valores.append(valor)
    for i in range(len(carros)):
        print('Produto: {}, Valor {:.2f} R$'.format(carros[i], valores[i]))

carros = ['Fusca','Gol','Brasilia', 'Clio', 'Marea']
valores = [10000, 15000, 20000, 25000, 300]

menu = int(input("Digite a Opção que deseja fazer \n 1 - Consultar Carros e Valores \n 2 - Remover Carro \n 3 - Adicionar um novo carro \n"))

match menu:
    case 1:
        consultar()
    case 2:
        removerCarros()
    case 3:
        adicionarCarro()
    case _:
        print('Digite um valor valido')
    