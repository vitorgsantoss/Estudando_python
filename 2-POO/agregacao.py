class Carrinho:
    def __init__(self):
        self._produtos= []

    def adicionar(self,*produtos):
        self._produtos.extend(produtos)

    def listar_produtos(self):
        for produto in self._produtos:
            print(f'Produto: {produto.nome}\nValor: {produto.preco}\n')
    
    def total(self):
        return sum(p.preco for p  in self._produtos)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# criando três produtos
p1, p2 = Produto('Skol lata', 6.00), Produto('Heineken longneck', 10.00)
p3 = Produto('Espeto', 6.00)
# criando o carrinho
carrinho = Carrinho()
# adicionando os produtos
carrinho.adicionar(p1,p2,p3)
# exibindo conteúdo carrinho
carrinho.listar_produtos()
# obtendo o valor total de produtos no carrinho
print('Valor total: ', carrinho.total())
