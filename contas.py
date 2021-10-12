class Cliente:
    def __init__(self, nome, cpf, profissao) -> None:
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero) -> None:
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0

        self.cliente = cliente
        self.__set_agencia = agencia
        self.__set_numero = numero

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = (30 / ContaCorrente.total_contas_criadas)

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, valor):
        if not isinstance(valor, int):
            raise ValueError(
                'O atributo agencia deve ser um número inteiro', valor)

        if valor <= 0:
            raise ValueError('O atributo agencia deve ser maior que 0')
        self.__agencia = valor

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, valor):
        if not isinstance(valor, int):
            raise ValueError('O atributo número deve ser um número inteiro')

        if valor <= 0:
            raise ValueError('O atributo número deve ser um número inteiro')
        self.__numero = valor

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError('O atributo saldo deve ser um número inteiro')

        if valor <= 0:
            raise ValueError('O atributo saldo deve ser um número inteiro')
        self.__saldo = valor

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


conta_corrente = ContaCorrente(None, '00', '101')


def main():
    import sys

    contas = []
    while(True):
        try:
            nome = input("Nome do cliente: \n")
            agencia = input("Número da agência: \n")
            breakpoint()
            numero = input("Número da conta corrente: \n")

            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append = conta_corrente
        except KeyboardInterrupt:
            print(f"\n\n {len(contas)} conta(s) criadas")
            sys.exit()

# if __name__ == "__main__":
#     main()
