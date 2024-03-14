import contas, pessoas, banco

cp1 = contas.Poupanca(2240, 232, 0)
cc1 = contas.Corrente(2205, 264, 0, 100)

c1 = pessoas.Cliente('Luis', 27, cc1)
c2 = pessoas.Cliente('Luis', 27, cp1)

b1 = banco.Banco()
b1.contas.extend([cp1,cc1])
b1.agencias.extend([cc1.agencia, cp1.agencia])
b1.clientes.extend([c1,c2])

if b1.autenticar(2205,c1):
    cc1.depositar(10)
    c1.conta.depositar(100)