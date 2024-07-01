import os

def cadastrarUsuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = senha
    print("Usuário cadastrado com sucesso!")

def removerUsuario():
    usuario = input("Digite o nome de usuário que deseja remover: ")
    if usuario in usuarios:
        del usuarios[usuario]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def listarUsuarios():
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(usuario)

def menu():
    global listaMenu
    listaMenu = int(input("1 - Cadastrar usuário\n2 - Remover usuário\n3 - Listar usuários\n4 - Sair"))

limparTela = lambda: os.system('cls' if os.name == 'nt' else 'clear')

usuarios = {
    "usuario1": "senha1",
    "usuario2": "senha2",
    "usuario3": "senha3"
}

tentativas = 4

admin = {
    "admin": "admin"
}

while tentativas > 0:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        print("Login bem-sucedido!")
        menu()
        while listaMenu != 4: 
            match listaMenu:
                case 1:
                    cadastrarUsuario()
                    menu()
                    limparTela()
                case 2:
                    removerUsuario()
                    menu()
                    limparTela()
                case 3:
                    listarUsuarios()
                    menu()
                    limparTela()
                case 4:
                    print("Saindo...")
                case _:
                    print("Opção inválida.")
        break
    else:
        tentativas -= 1
        print("Nome de usuário ou senha incorretos. Tente novamente.")

if tentativas == 0:
    print("Acesso bloqueado.")