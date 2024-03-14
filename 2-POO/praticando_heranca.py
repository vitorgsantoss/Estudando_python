class Animal: 
    def __init__(self,especie):
        self.especie = especie

    def make_sound(self, nome, som):
        print(f'{nome} pode {som}')

class Cachorro(Animal):
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome

lulu = Cachorro('cachorro')
lulu.nome='Lulu'
lulu.make_sound(lulu.nome, 'latir')