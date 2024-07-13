import os

estoque = {}
#produto e qntd

menu =  '''1- adicionar
2- Remover
3- Consultar
4- Sair
'''

def adicionar(nome, qnt):
    if nome in estoque:
        estoque[nome] = qnt + estoque[nome]
    else:
        estoque[nome] = qnt 
def remover(nome):
    if nome in estoque:
        del estoque[nome]
    else:
        print('produto não esta em estoque')

def consultar():
    print('------------------ ESTOQUE ----------------')
    for i,j in estoque.items():
        print('Produto:{}, Quantidade:{}'.format(i, j))
    print('-------------------------------------------')



while True:
    try:
        escolha = int(input(menu))
        continuar = True
        os.system('cls')
    except:
        continuar = False
    
    if continuar:
        match escolha:
            case 1:
                produto = input('informe o nome do produto')
                qnt = input('informe a quantidade de produto')
                adicionar(produto, qnt)
                os.system('cls')
                print('produto adicionado com sucesso')
            case 2:
                produto = input('informe o nome do produto')
                remover(produto)
                os.system('cls')
                print('removido com sucesso')
            case 3:
                os.system('cls')
                consultar()
            case 4:
                break
            case _:
                print('Opção invalido')