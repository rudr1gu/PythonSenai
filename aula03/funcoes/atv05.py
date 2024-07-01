def aniversario(nome):
    '''recebe o nome como argumento e muda as letras para maiusculo'''
    return nome.upper()

nome = input('Informe o nome do aniversariante: ')    
resultado = aniversario(nome)
print('Feliz aniversario {}'.format(resultado))