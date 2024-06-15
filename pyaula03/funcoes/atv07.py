def calcular(a,b,c = 0, d = 0, e = 0):
    '''calcula o resultado de a e b, se for é soma, 2 subtração, 3 multiplicação, 4 divisão'''
    match operador:
        case 1:
            resultado = a + b + c + d + e
            print('O Resultado da soma é:'.format(resultado))
        case 2:
            resultado = a - b - c - d - e
            print(resultado)
        case 3:
            if c == 0:
                resultado = a * b
                print(resultado)
            elif d == 0:
                resultado = a * b * c
                print(resultado)
            elif e == 0:
                resultado = a * b * c * d
                print(resultado)
            else:
                resultado = a * b * c * d * e
                print(resultado)
        case 4:
            if c == 0:
                resultado = a / b
                print(resultado)
            elif d == 0:
                resultado = a / b / c
                print(resultado)
            elif e == 0:
                resultado = a / b / c / d
                print(resultado)
            else:
                resultado = a / b / c / d / e
                print(resultado)
        case _:
            print('operador invalido')

operador = int(input('\n1 - Soma\n2 - Subtração \n3 - Multiplicação \n4 - Divisão \nInforme o operação que deseja:'))
n1 = int(input('\ninsira um numero: '))
n2 = int(input('\ninsira outro numero: '))

calcular(n1,n2,10,3)