produtos = ['abacaxi','pera','mamao','banana','umbu','caju','limao','manga','cigarro','cerveja']
valores = [10.20, 2.3,5.4,5.3,4.1,9.20, 7.3,4.4,5.6,7.1]

for i in range(len(produtos)):
    print('Produto: {}, Valor {:.2f}'.format(produtos[i], valores[i]))

def addProduto():
    produto = input('insira um novo produto')
    produtos.append(produto)
    valor = input('insira o valor do produto')
    valores.append(valor)

def consultarProduto():
    consulta = input('Insira o nome do produto: ')
    for i in range(len(produtos)):
        if consulta == produtos[i]:
            print('O Valor do produto: {} é de: {:.2f} R$'.format(produtos[i], valores[i]))
    