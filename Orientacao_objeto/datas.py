class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano 


    def formatada(self):
        self.dia = int(self.dia)
        self.mes = int(self.mes)
        self.ano = int(self.ano)
        print('\n{}/{}/{}'.format(self.dia, self.mes, self.ano))


