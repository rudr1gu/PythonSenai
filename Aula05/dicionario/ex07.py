import os
listaContatos = {}

def adicionarContato():
    qntd = int(input('Quantos contatos deseja adicionar? \n:'))
    for i in range(qntd):
        nome = input('Informe o nome do contato: ')
        telefone = input('Informe o numero da pessoa: ')
        email = input('Informe o email da pessoa: ')
        endereco = input('informe o endereco da pessoa: ')
        relacao = input('Qual tipo de relação: ')
        listaContatos[nome] = {'telefone': telefone,'email': email,'endereco': endereco, 'relacao': relacao}
    print('Contato salvo com sucesso')

def consultar():
    nome = input('Informe o nome')
    if nome in listaContatos:
        print('Telefone {} \nE-mail{}\nEndereço{}\n Relacao{}'.format(listaContatos[nome]['telefone'],listaContatos[nome]['email'],listaContatos[nome]['endereco'],listaContatos[nome]['relacao']))
        os.system('cls')
    else:
        print('Contato não existe!')

def showListaContatos():
    for nome, info in listaContatos.items():
        print('-- -- -- -- -- -- -- -- -- -- -- -- --')
        print('Nome: {}'.format(nome))
        print('-- -- -- -- -- -- -- -- -- -- -- -- --')

        if info['telefone'] != '':
            print('| - Telefone: {}'.format(info['telefone']))
        if info['email'] != '':
            print('| - E-mail: {}'.format(info['email']))
        if info['endereco'] != '':
            print('| - Endereço: {}'.format(info['endereco']))
        if info['relacao'] != '':
            print('| - Relação: {} \n-- -- -- -- -- -- -- -- -- -- -- -- --\n '.format(info['relacao']))
    


def remover():
    nome = input('informe o nome da pessoa que deseja remover')
    listaContatos.pop(nome)
    os.system('cls')
    print("removido com sucesso!")

def inputMenu():
    global menu
    menu = int(input('1 - Adicionar novo contato\n2 - Consultar contato\n3 - Ver lista de contatos\n4 - Remover um contato\n5 - Fechar\n :'))

inputMenu()

while menu != 5:
    match menu:
        case 1:
            os.system('cls')
            adicionarContato()
            inputMenu()
        case 2:
            os.system('cls')
            consultar()
            inputMenu()
        case 3:
            os.system('cls')
            showListaContatos()
            inputMenu()
        case 4:
            os.system('cls')
            remover()
            inputMenu()
        case _:
            print('[ERRO] Insira uma opção valida')