class Cliente:
    def __init__(self, nome, cpf, profissao) -> None:
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


cliente = Cliente('Richard Alves', 3976894087, 'Gamer')
print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)
