class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self,nome, salario, departamento):
        super().__init__(nome,salario)
        self.departamento = departamento

funcionario= Funcionario('José', 5000)
gerente = Gerente('Vítor', 20000, 'Dev back-end')
print(f'O gerende de {funcionario.nome} é {gerente.nome}')
print(f'Funcionario: {funcionario.nome}\nSalário: {funcionario.salario}\n')
print(f'Gerente: {gerente.nome}\nSalário: {gerente.salario}\n\
Área de atuação: {gerente.departamento}')