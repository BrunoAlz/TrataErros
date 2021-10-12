class ContaCorrente:
    total_contas_criadas = 0

    def __init__(self, cliente, agencia, numero) -> None:
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero

        ContaCorrente.total_contas_criadas += 1
        

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)
        

    def secar(self, valor):
        self.saldo -= valor
        

    def depositar(self, valor):
        self.saldo += valor
