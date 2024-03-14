from abc import ABC, abstractmethod

def my_repr(instancia):
    msg = ''
    for item, valor in instancia.__dict__.items():
        msg+= f'{item}: {valor}, '
    return msg


class Conta(ABC):
    def __init__(self, agencia: int, num_conta: int, saldo: float):
        self.agencia = agencia
        self.num = num_conta
        self.saldo = saldo

    def __repr__(self):
        return my_repr(self)


    def detalhes(self, msg=''):
        print(f'Seu saldo é {self.saldo}, {msg}')
        print('--'*10)

    @abstractmethod
    def sacar(self, valor: float) : ...
    
    def depositar(self, valor: float) -> float:
        self.saldo+=valor
        self.detalhes(f'depósito efetuado com sucesso, {valor}')
        return self.saldo

class Poupanca(Conta):
    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            self.detalhes(f'saque efetuado com sucesso, {valor:.2f}')
            return self.saldo
        print('Valor para saque inválido')
        self.detalhes(f'Saque negado, {valor:.2f}')


class Corrente(Conta):
    def __init__(self, agencia: int, num_conta: int, saldo: float, limite: float):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        if valor<=(self.saldo+self.limite):
            self.saldo-=valor
            self.detalhes(f'saque efetuado com sucesso, {valor}')
            return self.saldo
        self.detalhes(f'valor de saque inválido, {valor}')
        