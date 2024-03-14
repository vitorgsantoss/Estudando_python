class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._engine = None
        self._manufacturer = None
        
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self,nome):
        self._engine = nome

    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,nome):
        self._manufacturer = nome


class Motor: 
    def __init__(self, model):
        self.model = model


class Fabricante: 
    def __init__(self, nome):
        self.nome = nome
        

vectra, corsa = Carro('Vectra'), Carro('Corsa')
v8 = Motor('v8')
fab1 = Fabricante('Chevrolet')

vectra.engine = v8
vectra.manufacturer = fab1

print(f'{vectra.manufacturer.nome}´s {vectra.nome} car has a {vectra.engine.model} engine')