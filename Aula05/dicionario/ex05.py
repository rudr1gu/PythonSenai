# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista. O programa deve ter as mesmas funcionalidades, mas agora deve ser possível adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo, se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave e 2 como valor. A estrutura do dicionário ficaria assim: {"banana": 2}.

listaDeCompras = {'Arroz':12}


def adicionarproduto():
    qntdDeProdutos = int(input('Informe quantos produtos deseja adicionar: \n'))
    for i in range(qntdDeProdutos):
        produto = input('Informe o nome do produto: \n')
        qntd = int(input('Informe a quantidade de produtos: \n'))
        listaDeCompras[produto] = qntd
    print(listaDeCompras)

def removerProduto():
    produto = input('informe o nome do produto que deseja remover')
    if produto in listaDeCompras:
        listaDeCompras.pop(produto)
        print(listaDeCompras)
    else:
        print('Não tem esse produto na lista de compras')

def consultar():
    print(listaDeCompras)

def inputMenu():
    global menu
    menu = int(input('1 - Adicionar Produto\n2 - Remover Item\n3 - Consulta lista \n4 - Sair\n:'))

inputMenu()
while menu != 4:
    match menu:
        case 1:
            adicionarproduto()
            inputMenu()
        case 2:
            removerProduto()
            inputMenu()
        case 3:
            consultar()
            inputMenu()
        case _:
            print('informe um numero de 1 ao 3')
            inputMenu()
