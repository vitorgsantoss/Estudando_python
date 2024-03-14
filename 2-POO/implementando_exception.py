# class MyError(Exception):
    
#     pass


# class OtherError(Exception):
#     pass


# def levantar():
#     exception_ = MyError('bla','ble','bli')
#     exception_.add_note('Você errou')
#     exception_.add_note('Erro número 1')
#     raise exception_
    
# try:
#     levantar()
# except MyError as error:
#     print(error.args)
#     print(error.__class__.__name__)
#     print()
#     exception_ = OtherError('Lançando erro secundário')
#     exception_.__notes__ = error.__notes__.copy()
#     raise exception_ from error
print(f'{"Vítor"!s}')