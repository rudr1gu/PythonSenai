cpf = input('Digite seu CPF').strip().replace('.','').replace('-','')


if len(cpf) == 11:
    print('Seu cpf esta correto ele tem 11 digitos')
else:
    print('tem mais de 11 digitos')

cpf = cpf.strip()
print(cpf)


print('cpf: ', cpf)