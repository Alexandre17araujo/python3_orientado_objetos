from validar import Carro, Moto
from controle import Controle

def rodar_carro():
    veiculo = Carro(22, 70, 'prata')

    mudar = veiculo.rodas = 17
    mudar2 = veiculo.cor = 'verde'
    #veiculo.km_rodados()

    veiculo.km_rodados()
    veiculo.km_rodados()
    veiculo.km_rodados()
    print('A cor do carro é {} e KM Rodados: {}'.format(mudar2, veiculo.rodados))
    print('O tamanho do aro é {}'.format(mudar))

def rodar_moto():
    motocicleta = Moto('novo', 'preto', '600 cilindradas')

    minha_moto1 = motocicleta.cor = 'cinza'
    minha_moto2 = motocicleta.motor = 'motor novo'
    
    print('O pneu da moto é {}'.format(motocicleta.pneus))


def controle_remoto():
    funcoes = Controle('volume_down', 'volume_up', 'canal_cima', 'canal_baixo')
    
    funcao_controle_volume_cima = funcoes.mudar_canal_cima
    funcao_controle_volume_baixo = funcoes.mudar_canal_baixo = 'Descendo canal'
    funcao_controle_canal_cima = funcoes.maior_volume = 'Almentando volume'
    funcao_controle_canal_baixo = funcoes.menor_volume

    
    print('Mudar canal para cima com o botão {}'.format(funcao_controle_canal_cima))
    print('Mudar canal para baixo com o botão {}'.format(funcao_controle_canal_baixo))
    print('Almentar volume cima com o botão {}'.format(funcao_controle_volume_cima))
    print('Diminuir volume baixo com o botão {}'.format(funcao_controle_volume_baixo))
    





#if __name__=='__main__':
    #controle_remoto()    


