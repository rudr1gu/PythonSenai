salario = input('insira o seu salario')
combustivel = input('insira seus gastos com combustivel')
bebida = input('insira seus gastos com bebida')
aluguel = input('insira seus gastos com aluguel')

liquido = int(salario) - int(combustivel) - int(bebida) - int(aluguel)

print(liquido)
print('O seu salario liquido é de R${:.2f}'.format(liquido))