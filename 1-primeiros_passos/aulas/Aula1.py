'''
Convertendo um número para hexadecimal com interpolação em python
em interpolação, os números são representados por seus tipos, sendo: 
%i ou %d para int
%f para float
%s para 
Você pode escrever o número hexadecimal em maiúsculo ou minúsculo, alterando entre %x ou %X na interpolação
'''
# Para colocar vária linha como comentário basta apertar ctrl+;
num = int(input('Informe o número que deseja convertar para hexadecimal: '))
print('O número %i em hexadecimal é %X'%(num,num))

# Também se pode escolher o número de casa que o número hexadecimal vai ocupar, segue o exemplo:
hexa = ('%05X'%(num))
print(hexa)
print(len(str(hexa)))
# Se o hexadecimal acima possuir menos de cinco casas elas serão preenchidas com 0 no exemplo

