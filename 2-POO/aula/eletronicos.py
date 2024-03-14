from log import LogFileMixin

class Eletronico():
    def __init__(self,nome):
        self._nome= nome
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True
        
    def desligar(self):
        if self._ligado:
            self._ligado = False
    

class Celulares(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)
    
    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)

# Teste com composição:
# class Celulares(Eletronico):
#     def __init__(self, nome):
#         super().__init__(nome)
#         self.log_cel = LogFileMixin()
#     def ligar(self):
#         super().ligar()
#         if self._ligado:
#             msg = f'{self._nome} está ligado'
#             self.log_cel.log_success(msg)
    
#     def desligar(self):
#         super().desligar()
#         if not self._ligado:
#             msg = f'{self._nome} está desligado'
#             self.log_cel.log_error(msg)
