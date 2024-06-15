opMenu = '\n1 - ir a página principal \n2 - ir a tela de login \n3 - ir para tela de pesquisa \n4 - logoff'
print(opMenu)

menu = int(input('\nInsira a uma opção do menu:  '))

match menu:
    case 1:
        print('Página principal')
    case 2:
        print('ir a tela de login')
    case 3:
        print('ir para tela de pesquisa')
    case 4:
        print('logoff')
