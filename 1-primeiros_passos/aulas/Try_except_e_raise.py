# try:
#     print(2/'0')
# # except (ZeroDivisionError, IndexError):
# #     print('Zero division or index error')
# except Exception as error:
#     if error.__class__ == ZeroDivisionError:
#         raise ('Dividiu por zero')
#     elif error.__class__ == TypeError:
#         raise TypeError('Erro de tipo')
# finally:
#     print('Finalizamos')
import sys
print(sys.platform)