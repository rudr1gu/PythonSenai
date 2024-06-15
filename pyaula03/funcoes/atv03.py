def aniversario():
    '''pergunta o nome do usuario'''
    nome =  input('Qual é seu nome?').upper()
    return nome
    
resultado = aniversario()
print('Feliz aniversario {}'.format(resultado))