cpf = input('Digite seu CPF')
cpf = cpf.strip()
print(cpf)

if len(cpf) == 11:
    print('Seu cpf esta correto ele tem 11 digitos')
else:
    print('digite um cpf valido')

