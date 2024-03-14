dicio = {
    'Pergunta':'Quanto é 5x5?',
    'Opções': [20,35,25,10],
    'Resposta': 25,
}
print(dicio['Pergunta'])
for cont, opc in enumerate(dicio['Opções']):
    print(f'{cont}) {opc}')
res=int(input('Resposta: '))
if res == dicio['Resposta']:
    print('Você acertou!')
    exit()
print('Você acertou!' if dicio['Opções'][res] == dicio['Resposta'] else 'Você errou!')