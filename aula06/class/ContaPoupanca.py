#Banco Python

# Todas elas devem ter características como Saldo, cheque especial, numero da conta, cpf, nome do correntista, agencia, limite pix noturno e diurno.
# Também devem ter métodos (ações) como: transferências, consultas, pagamentos e encerramento de conta..

class ContaPoupanca:

    def __init__(self, nome: str, cpf: str , numeroConta: int, saldo: float):
        self.nome: str = nome
        self.cpf: str = cpf
        self.numeroConta: int = numeroConta
        self.saldo: float = saldo
        self.agencia: str = '2834-4'
        self.limitePixNoturno: float = 0
        self.limitePixDiurno: float = 0
        self.chequeEspecial: float = 0

    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome: str = nome
    
    def getCpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf: str = cpf
    
    def getNumeroConta(self):
        return self.numeroConta
    def setNumeroConta(self, numeroConta):
        self.numeroConta: int = numeroConta
    
    def getSaldo(self):
        return self.saldo
    def setSaldo(self, saldo):
        self.saldo: float = saldo
    
    def depositar(self, valor: float):
        self.saldo += valor
        print('Depósito realizado com sucesso!')

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente')
    
    def consultar(self):
        print('---------------------------------------------')
        print('Nome: {}\nCPF: {} \nNúmero da conta: {}\nSaldo: {}'.format(self.getNome(), self.getCpf() , self.getNumeroConta(), self.getSaldo()))
        print('---------------------------------------------')
    def transferir(self, contaDestino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            contaDestino.depositar(valor)
            print('Transferência realizada com sucesso!')
        else:
            print('Saldo insuficiente')
