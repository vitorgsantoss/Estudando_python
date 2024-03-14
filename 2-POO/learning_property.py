class Carro():
    def __init__(self):
        self._modelo= None
    
    @property
    def modelo(self):
        return self._modelo
    # @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo
        
        
vectra = Carro()
print(vectra.modelo)
vectra.modelo = 'Vectra'
print(vectra.modelo)