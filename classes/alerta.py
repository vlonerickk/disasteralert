class Alerta:
    def __init__(self, tipo, mensagem, nivel_risco):
        self.tipo = tipo
        self.mensagem = mensagem
        self.nivel_risco = nivel_risco

    def enviar_alerta(self, destinatario, meio="email"):
        return f"Alerta '{self.tipo}' enviado para {destinatario} via {meio}: {self.mensagem}"

    def __str__(self):
        return f"[{self.tipo}] Nível: {self.nivel_risco} - {self.mensagem}"
