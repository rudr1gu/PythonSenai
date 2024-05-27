numero = int(input("insira o valor do seu salario: "))

if numero < 1412:
    print('Você ganha menos que um salario minimo')
elif numero == 1412:
    print('Você ganha um salario minimo')
else:
    if numero < 10000:
        print('ta vivendo')
    else:
        print('Ai é luxo!')