class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    def getnome(self):
        return self.__nome

p1 = Pessoa('Vítor')
print(p1.getnome())