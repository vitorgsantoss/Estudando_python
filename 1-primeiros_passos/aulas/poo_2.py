import json

with open('Carros.json', 'r') as arquivo:
    cars = json.load(arquivo)

print(cars)