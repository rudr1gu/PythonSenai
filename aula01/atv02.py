idade = int(input('insira sua idade: '))

if idade < 18:
    print('Adolecente')
elif idade == 18 or idade <= 28:
    print('Jovem')
elif idade < 45:
    print('Adulto')
else:
    print('Senior')