import json

class Carro:
    def __init__(self,nome, valor, ano):
        self.nome = nome
        self.valor = valor
        self.ano = ano
    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('fusca', 7000, 1980)
corsa = Carro('corsa',22000,2010)

bd_cars = fusca.__dict__,corsa.__dict__

with open("Carros.json",'w', encoding='utf8') as arquivo:
    json.dump(
        bd_cars,
        arquivo,
        ensure_ascii= False,
        indent= 2
    )