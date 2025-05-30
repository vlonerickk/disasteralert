class Desastre:
    def __init__(self, tipo, data, localizacao, severidade):
        self.tipo = tipo
        self.data = data
        self.localizacao = localizacao
        self.severidade = severidade

    def gerar_descricao(self):
        return f"{self.tipo} em {self.localizacao.cidade} ({self.data}) - Severidade: {self.severidade}"

    def __str__(self):
        return self.gerar_descricao()
