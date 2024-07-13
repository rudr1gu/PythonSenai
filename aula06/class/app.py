import os
from ContaPoupanca import ContaPoupanca

menu = '''
1 - Consultar
2 - Depositar
3 - Sacar
4 - Transferir
5 - Definir limite diurno
6 - Definir limite noturno
7 - Sair
'''

conta2 = ContaPoupanca('José', '123.321.234-56',1234, 1000)

while True:
    print(menu)
    opcao = int(input('Digite a opção desejada: '))
    match opcao:
        case 1:
            os.system('cls')
            conta2.consultar()
        case 2:
            valor = float(input('Digite o valor do depósito: '))
            conta2.depositar(valor)
            os.system('cls')
            print('Depósito realizado com sucesso!')
        case 3:
            valor = float(input('Digite o valor do saque: '))
            conta2.sacar(valor)
            os.system('cls')
            print('Saque realizado com sucesso!')
        case 4:
            valor = float(input('Digite o valor da transferência: '))
            contaDestino = ContaPoupanca('Maria', '321.123.456-78', 4321, 500)
            conta2.transferir(contaDestino, valor)
            os.system('cls')
            print('Transferência realizada com sucesso!')
        case 5:
            valor = float(input('Digite o valor do limite diurno: '))
            conta2.limitePixDiurno = valor
            os.system('cls')
            print('Limite diurno definido com sucesso!')
        case 6:
            valor = float(input('Digite o valor do limite noturno: '))
            conta2.limitePixNoturno = valor
            os.system('cls')
            print('Limite noturno definido com sucesso!')
        case 7:
            os.system('cls')
            print('Saindo...')
            break
        case _:
            print('Opção inválida')