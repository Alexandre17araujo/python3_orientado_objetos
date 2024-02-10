class Controle:
    def __init__(self, menor_volume, maior_volume, mudar_canal_cima, mudar_canal_baixo):
        self.__menor_volume = menor_volume
        self.__maior_volume = maior_volume
        self.__mudar_canal_cima = mudar_canal_cima
        self.__mudar_canal_baixo = mudar_canal_baixo


    @property
    def menor_volume(self):
        return self.__menor_volume
    @menor_volume.setter
    def menor_volume(self, mudando_volume_menor):
        self.__menor_volume = mudando_volume_menor

    @property
    def maior_volume(self):
        return self.__maior_volume
    @maior_volume.setter
    def maior_volume(self, mudando_volume_maior):
        self.__maior_volume = mudando_volume_maior

    @property
    def mudar_canal_cima(self):
        return self.__mudar_canal_cima
    @mudar_canal_cima.setter
    def mudar_canal_cima(self, trocando_canal_cima):
        self.__mudar_canal_cima = trocando_canal_cima

    @property
    def mudar_canal_baixo(self):
        return self.__mudar_canal_baixo
    @mudar_canal_baixo.setter
    def mudar_canal_baixo(self, trocar_canal_baixo):
        self.__mudar_canal_baixo = trocar_canal_baixo
