from os import system
import secrets
import string as s
from secrets import SystemRandom as Sr

system('cls')

random = secrets.SystemRandom()#deixa o padrão do random realmente aleatório
# sendo assim, mais seguro
# EXEMPLO
# clientes = ['Ruan', 'Alef', 'Lyon', 'Jader', 'Mari', 'Negueba']
# clientes_aleatorios = random.sample(clientes, k=2)
# print(clientes_aleatorios)

# CRIANDO SENHA ALEATÓRIA SEGURA
senha = s.ascii_letters+s.digits+s.punctuation
# concatena todas as letras (maiúsculas e minúsculas) + digitos + pontuações do
# módulo string
senha = Sr().choices(senha, k = 8)
# retorna uma lista com k elementos aleatórios da string senha acima (podendo 
# ter elementos repitidos)
senha= ''.join(senha)
# une a lista em uma única string
print(senha)