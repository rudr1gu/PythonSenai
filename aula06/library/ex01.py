#Bibliotecas Python
import random #Biblioteca para gerar números aleatórios

a = random.uniform(1, 100) #Gera um número aleatório entre 1 e 100 float
b = random.randint(1, 100) #Gera um número aleatório entre 1 e 100 inteiros

print('uniforme{:.2f}, radiant{}'.format(a,b))

numero = int(input('Digite um número de 0 a 100: '))
while True:
    if numero == a:
        print('Parabéns, você acertou!')
        break
    elif numero > a:
        print('O número é menor')
    else:
        print('O número é maior')
    print('Parabéns, você acertou!')

