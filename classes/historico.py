class Historico:
    def __init__(self):
        self.desastres = []
        self.alertas = []

    def adicionar_desastre(self, desastre):
        self.desastres.append(desastre)

    def adicionar_alerta(self, alerta):
        self.alertas.append(alerta)

    def listar_desastres(self):
        return self.desastres

    def listar_alertas(self):
        return self.alertas
