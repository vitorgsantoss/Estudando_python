while True:
    cpf= str(input('Informe o CPF: '))
    if not cpf.isnumeric():
        try:
            cpf=cpf.replace('.','')
            cpf=cpf.replace('-','')
            
        except:
            print('Tivemos um problema técnico, por favor digite seu cpf novamente')
        
    if len(cpf)==11:
        break
    else:
        print('Tamanho de cpf inválido, por favor, tente novamente')

cpf_9= list(cpf[:10])
contador=0
num=0

for i in range(10,1,-1):
    num+= i*int(cpf_9[contador])
    contador+=1
num*=10
num%=11
digito= 0 if num>9 else num

if digito == int(cpf[-2]):
    print('Este CPF é válido')
else:
    print('Este CPF é inválido')