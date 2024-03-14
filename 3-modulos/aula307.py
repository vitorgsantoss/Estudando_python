from argparse import ArgumentParser

parse = ArgumentParser()
parse.add_argument(
    '-b', '--basic',
    help = 'Script para teste de ArgumentParser', #define uma mensagem de ajuda caso -b -h seja chamado
    # type= str, define o tipo de dado a ser armazenado em parse.basic
    metavar= 'STRING',
    action= 'append', #prepara parse.basic para trabalhar com listas
    # default='Hello World',  define um valor padrão caso -b não seja chamado no terminal
    # required = False) coloca o argumento como obrigatório ou não
)
parse.add_argument(
    '-v', '--verbose',
    help= 'retorna true or false',
    action= 'store_true',
)
args = parse.parse_args()
# print('valor padrão de: ',args.basic)
print(args.basic)
print(args.verbose)