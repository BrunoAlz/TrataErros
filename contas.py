class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero) -> None:
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = (30 / ContaCorrente.total_contas_criadas)



    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)


    def secar(self, valor):
        self.saldo -= valor
        

    def depositar(self, valor):
        self.saldo += valor


conta_corrente = ContaCorrente(None, '00', '101')
