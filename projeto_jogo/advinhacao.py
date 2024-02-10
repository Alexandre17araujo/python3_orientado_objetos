import random

def jogar():
    print('#' * 30)
    print('     Jogo da ADVINHAÇÃO')
    print('#' * 30)

    #numero_secreto = int(random.random() * 100)
    numero_secreto = int(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print(numero_secreto)

    print('')
    print('Niveis de dificuldades')
    print('(1)Facil, (2)Médio, (3)Difícil \n')


    nivel = int(input('Informe o nível que deseja: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Digite um numero entre 1 e 100: '))
        print('Você digitou {}'.format(chute))

        if (chute < 1 or chute > 100):
            print('Você deve digita um número entre 1 e 100 !') 
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Você acertou !!! E fez {} pontos'.format(pontos))
            break
        else:
            if (maior):
                print('Você ERROU ! Você informou um valor maior que o valor secreto !')
                if rodada == total_de_tentativas:
                    print('O número secreto era {}. Você fez {} pontos.'.format(numero_secreto, pontos))
            elif (menor):
                print('Você ERROU ! Você informou um valor menor que o numero secreto !')
                if rodada == total_de_tentativas:
                    print('O número secreto era {}. Você fez {} pontos.'.format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print('Gamer Over')

if (__name__=="__main__"):
    jogar()