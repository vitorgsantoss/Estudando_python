from typing import Any


class Ligação:
    def __init__(self,numero):
        self.numero = numero

    def __call__(self, nome):
        print(f'{nome}, está te ligando. {self.numero}')
        return 'Perdida'

call1= Ligação(15997592983)
print(call1('Vítor'))
