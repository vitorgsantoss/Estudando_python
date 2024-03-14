# Crie uma classe abstrata chamada FiguraGeometrica com métodos abstratos 
# calcular_area() e calcular_perimetro(). Em seguida, crie uma classe abstrata 
# chamada Colorida com um método abstrato definir_cor(). Crie uma classe chamada 
# Retangulo que herde de ambas as classes abstratas FiguraGeometrica e Colorida.
# Implemente os métodos abstratos em Retangulo para calcular a área e o perímetro 
# de um retângulo e definir sua cor. Crie uma instância de Retangulo e teste os 
# métodos implementados.
from abc import ABCMeta, abstractmethod, ABC

class FiguraGeometrica(metaclass = ABCMeta):
    @abstractmethod
    def calcular_area(self):
        ...
    
    @abstractmethod
    def calcular_perimetro(self):
        ...


class Colorida(ABC):
    
    @property
    def definir_cor(self):
        return self._cor

    @definir_cor.setter
    @abstractmethod
    def definir_cor(self):
        ...


class Retangulo(FiguraGeometrica,Colorida):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self._cor = None
    def calcular_area(self):
        area = self.altura * self.largura
        return area
    
    def calcular_perimetro(self):
        perimetro = (self.altura + self.largura)*2
        return perimetro
    
    @Colorida.definir_cor.setter
    def definir_cor(self,cor):
        self._cor = cor

def exibir_figura(objeto):
    print('A altura do objeto é: ', objeto.altura)
    print('A largura do objeto é: ', objeto.largura)
    print('A área do objeto é: ', objeto.calcular_area())
    print('O perímetro do objeto é: ', objeto.calcular_perimetro())
    print(f'A cor do {objeto.__class__.__name__} é {objeto.definir_cor}')

retangulo = Retangulo(4,9)
retangulo.definir_cor = 'rosa'
exibir_figura(retangulo)