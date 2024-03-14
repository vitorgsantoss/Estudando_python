from pathlib import Path

register_way = Path(__file__).parent / 'log_register.txt'

class Log:
    def _log(self,msg):
        raise NotImplementedError('Log não implementadado')
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg} ')

    def log_success(self, msg):
        return self._log(f'Sucesso: {msg} ')


class LogFileMixin(Log):
    def _log(self,msg):
        msg_formata = f'{msg} ({__class__.__name__})'
        with open(register_way,'a',encoding='utf8') as arquivo:
            arquivo.write(msg_formata)
            arquivo.write('\r\n')


class LogPrintMixing(Log):
    def _log(self,msg):
        print(f'{msg} ({__class__.__name__})')


if __name__ == '__main__':
    ...
