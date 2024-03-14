def my_repr(self):
    return f'{type(self).__name__}: {self.__dict__}'

class Meta(type):
    def __new__(mcs, name, bases, dict):
        cls = super().__new__(mcs, name, bases, dict)
        # cls.falar = 'ululu'
        print('Estou no new')
        
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implementente falar')
        return cls
    
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        print(cls.__dict__)
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Informe um nome')
        return instancia
    
    

class Pessoa(metaclass = Meta):
    def __init__(self, nome):
        ...
        self.nome = nome
        

    def falar(self):
       return 'FALANDO'

p1 = Pessoa('Vítor')
print(p1.nome)
print(p1.falar())
print(my_repr(p1))