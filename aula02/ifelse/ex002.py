empresaVendas = int(input('Insira o valor de vendas da empresa: '))

if empresaVendas >= 200000:
    vendedor = int(input('insira o valor de vendas do vendedor: '))
    
    if vendedor >= 30000:
        print('Vendedor recebeu um bonus de {}'.format(.2*vendedor))
    elif vendedor >= 15000:
        print('Vendedor recebeu um bonus de {}'.format(.1*vendedor))
    else:
        print('Vendedor não bateu a meta')
else:
    print('empresa não bateu a meta')