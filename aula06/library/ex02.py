#jogo da forca com animais
import random

animais = ['cachorro', 'gato', 'elefante', 'leão', 'tigre', 'girafa', 'zebra', 'macaco', 'panda', 'coala', 'urso', 'lobo', 'rinoceronte', 'hipopótamo', 'golfinho', 'baleia', 'peixe', 'pássaro', 'cobra', 'lagarto', 'aranha', 'escorpião', 'abelha', 'borboleta', 'formiga', 'abelha', 'gafanhoto', 'camelo', 'cavalo', 'vaca']

carros = ['fusca','kombi','brasilia','chevette','camaro','mustang','maverick', 'opala', 'corcel', 'landau', 'galaxie', 'ferrari', 'lamborghini', 'porsche']

nomes = ['josue','moises','davi','salomao','daniel','isaias','jeremias','elias','eliseu','samuel','saul']

times = ['flamengo','vasco','botafogo','fluminense','corinthians','palmeiras','santos','são paulo','cruzeiro','atlético-mg','internacional','grêmio','bahia','vitória','sport','náutico','santa cruz','fortaleza','ceará','criciúma','figueirense']

def tema():
    print('''Escolha um tema:
          1 - Animais
          2 - Carros
          3 - Nomes
          4 - Times de futebol''')
    tema = input('Digite o número do tema: ')
    if tema == '1':
        jogar(animais)
    elif tema == '2':
        jogar(carros)
    elif tema == '3':
        jogar(nomes)
    elif tema == '4':
        jogar(times)
    else:
        print('Tema inválido')
        tema()


def jogar(tema):
    palavra = random.choice(tema)
    palavra_secreta = []
    
    for letra in palavra:
        palavra_secreta.append('_')
    print(' '.join(palavra_secreta))

    tentativas = 10
    while tentativas > 0:
        letra = input('Digite uma letra: ')
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra
            print(' '.join(palavra_secreta))
        else:
            tentativas -= 1
            print('Você errou! Restam {} tentativas'.format(tentativas))
        if '_' not in palavra_secreta:
            print('Parabéns, você acertou a palavra!')
            break
    if tentativas == 0:
        print('Que pena, você perdeu! A palavra era {}'.format(palavra))

tema()