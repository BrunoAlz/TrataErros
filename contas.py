class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero) -> None:
        self.__saldo = 100
        self.cliente = cliente
        self.__agencia = agencia
        self.__numero = numero

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = (30 / ContaCorrente.total_contas_criadas)

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, valor):

        if not isinstance(valor, int):
            return

        if valor <= 0:
            return

        self.__agencia = valor


    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):

        if not isinstance(valor, int):
            return

        if valor <= 0:
            return

        self.__numero = valor
        
        
        
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):

        if not isinstance(valor, int):
            return

        if valor <= 0:
            return

        self.__saldo = valor
                
        
        
        

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def secar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


conta_corrente = ContaCorrente(None, '00', '101')
