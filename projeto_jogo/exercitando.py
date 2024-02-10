import random


def jogar():
    print('')
    print('*' * 40)
    print(' Faça login para iniciar o joguinho !')
    print('*' * 40)
    print('')


    def login():
        usuario = input('Informe seu login: ')
        if usuario == 'alex':
            print('\nEntrada de usuario \033[1;36m{}\033[m.\n'.format(usuario))

            senha = input('Informe sua senha: ')
            if senha == 'root':
                print('\033[1;32m Login efetuado com sucesso !!!\033[m \n')
                joguinho()
            else:
                print('\033[1;31mLogin não efetuado !!!\033[m')
        else:
            print('\n\033[1;31mUsuário não identificado !!!\033[m')

    def joguinho():
        print('\033[1;35m Vamos iniciar o jogo\033[m \n')

        numero_secreto = int(random.randrange(1, 101))
        tentativas = 0
        pontos = 1000
        
        print('\nSelecione algum nível\n')
        print('(1) Facíl, (2)Médio, (3)Difícil\n')
        
        niveis = int(input('Selecione algum nível: '))

        if niveis == 1:
            tentativas = 20
        elif niveis == 2:
            tentativas = 10
        else:
            tentativas = 5
    

        for rodada in range(1, tentativas + 1):
            print('\n\033[1;31m{}\033[m tentativas de \033[1;32m{}\033[m'.format(rodada, tentativas))
            chute = int(input('\nInforme um valor de 1 até 100: '))
            
            if (chute < 1 or chute > 100):
                print('\033[1;31mInforme o valo entre 1 até 100 !!! \033[m')
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto
            
            if (acertou):
                print('\033[1;32mAcertou !!!\033[m')
                print('Você fez {} pontos.'.format(pontos))
                break
            elif (maior):
                print('Você informou um valor \033[1;31mMAIOR\033[m que o número secreto !')
            else:
                print('Você informou um valor \033[1;31mMENOR\033[m que o número secreto !')
            if rodada == tentativas:
                print('\nO valor secreto é {} e fez {} pontos.'.format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = (pontos - pontos_perdidos)




    logar = input('Deseja fazer login? S/N: ').upper()
    if logar == 'S':
        login()
        
    else:
        print('\033[1;31mSAINDO\033[m')
if __name__=="__main__":
    jogar()
