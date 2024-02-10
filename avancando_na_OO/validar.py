class Carro:
    def __init__(self, rodas, vidros, cor):
        self.__rodas = rodas
        self.__vidros =vidros
        self.__cor = cor
        self.__rodados = 0

    @property
    def rodas(self):
        return self.__rodas
    
    @rodas.setter
    def rodas(self, novas_rodas):
        self.__rodas = novas_rodas

    @property
    def rodados(self):
        return self.__rodados

    def km_rodados(self):
        self.__rodados += 10

class Moto:
    def __init__(self, pneus, cor, motor):
        self.pneus = pneus
        self.__cor = cor.title()
        self.__motor = motor
        self.__rodados = 0
        

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor.title()


    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, novo_motor):
        self.__motor = novo_motor.title()
    
    def km_rodados(self):
        self.__rodados += 5


