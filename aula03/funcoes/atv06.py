saldo = 0

def sacar(valor):
    '''subtrai o valor do saldo'''
    global saldo
    saldo -= valor
    return saldo

def depositar(valor):
    '''soma o valor do saldo'''
    global saldo
    saldo += valor
    return saldo

def consultarSaldo(saldo):
    '''mostra o saldo'''
    print(saldo)

depositar(100)
sacar(20)
consultarSaldo(saldo)