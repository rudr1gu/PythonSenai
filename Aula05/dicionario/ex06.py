#Crie um aagenda de telefone: Cada pessoa devera receber um numero especifico
listaContatos = {}

def adicionarContato():
    nome = input('Informe o nome do contato: ')
    telefone = input('Informe o numero da pessoa: ')
    listaContatos[nome] = telefone
    print(listaContatos)

adicionarContato()