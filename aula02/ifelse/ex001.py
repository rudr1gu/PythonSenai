age = int(input('insira sua idade'))

if age < 18:
    print('Adolecente')
elif age == 18 or age <=28:
    print('Jovem')
elif age < 45:
    print('Adulto')
else:
    print('senior')