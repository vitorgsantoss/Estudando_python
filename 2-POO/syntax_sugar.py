# def meu_decorador(funcao):
#     def nova_funcao():
#         print("Executando código antes da função original.")
#         funcao()
#         print("Executando código depois da função original.")
#     return nova_funcao

# @meu_decorador
# def minha_funcao():
#     print("Minha função original.")
#     return 2

# print(minha_funcao())

def decorador_com_parametros(parametro):
    def decorador_real(funcao):
        def wrapper(*args, **kwargs):
            print(f"Parâmetro do decorador: {parametro}")
            resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return decorador_real

@decorador_com_parametros("Algo")
def funcao_decorada():
    print("Função decorada.")

funcao_decorada()