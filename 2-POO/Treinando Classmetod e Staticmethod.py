class Animal():
    qtd = 0
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        Animal.cont()

    @classmethod
    def cont(cls):
        cls.qtd+=1

a1 = Animal('Leão', 'Felino')
a2 = Animal('Cobra', 'Réptil')
print(Animal.qtd)

