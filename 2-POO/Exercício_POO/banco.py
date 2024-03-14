import contas, pessoas


class Banco:
    def __init__(self,
                 agencia: list[int] | None = None,
                 conta: list[contas.Conta] | None = None,
                 cliente: list[pessoas.Pessoa] | None = None):
        self.agencias = agencia or []
        self.contas = conta or []
        self.clientes = cliente or []

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f':\n({self.agencias}\n{self.clientes}\n{self.contas})'
        return f'{class_name}{attrs}'
    
    def checa_conta(self, conta):
        if conta in self.contas:
            return True
        print('Estou no checar conta', False)
        return False
    
    def checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        print('Estou no checar cliente', False)
        return False
    
    def checa_agencia(self, agencia):
        if agencia in self.agencias:
            return True
        print('Estou no checar agencia', False)
        return False
    
    def checa_conta_cliente(self, agencia, cliente: pessoas.Cliente):
        if agencia == cliente.conta.agencia:
            return True
        print('Estou no checar se conta é do cliente', False)
        return False
    
    def autenticar(self, agencia, cliente):
        if self.checa_conta(cliente.conta)\
        and self.checa_agencia(agencia)\
        and self.checa_cliente(cliente)\
        and self.checa_conta_cliente(agencia, cliente):
            return True
        return False
    