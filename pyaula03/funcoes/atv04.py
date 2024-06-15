def calcular(a,b):
    '''calcula o resultado de a e b, se for é soma, 2 subtração, 3 multiplicação, 4 divisão'''
    match operador:
        case 1:
            resultado = a + b
            print('O Resultado da soma é:'.format(resultado))
        case 2:
            resultado = a - b
            print(resultado)
        case 3:
            resultado = a * b
            print(resultado)
        case 4:
            resultado = a / b
            print(resultado)
        case _:
            print('operador invalido')

operador = int(input('\n1 - Soma\n2 - Subtração \n3 - Multiplicação \n4 - Divisão \nInforme o operação que deseja:'))
n1 = int(input('\ninsira um numero: '))
n2 = int(input('\ninsira outro numero: '))

calcular(n1,n2) 