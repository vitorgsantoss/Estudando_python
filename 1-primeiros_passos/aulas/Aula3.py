nome= 'Vítor'
idade = 19
print(f'{nome= }: {idade= } anos')
while True:
    sair= input('Deseja sair? S/N ').lower().startswith('s')
    if sair:
        break
    else:
        print('Você escolheu continuar')
print('Você saiu do laço de repetição')
print('\t testando a função para dar espaço')