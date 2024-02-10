import forca
import advinhacao

print('*' * 30)
print('       Escolha seu jogo')
print('*' * 30)

print('\n(1) Jogo da FORCA, (2) Jogo da advinhação')

jogo = int(input('Informe qual o jogo: '))

if (jogo == 1):
    print('Jogando forca')
    forca.jogar()
elif (jogo == 2):
    print('Jogando advinhação')
    advinhacao.jogar()