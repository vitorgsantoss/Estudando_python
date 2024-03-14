from datetime import datetime

def ln():
    print('-'*40)
    

fmt_data = '%d/%m/%Y'
fmt_hora = '%H:%M'

data_hora = datetime.now().replace(microsecond=0)
data = datetime.strftime(data_hora, fmt_data)
hora = datetime.strftime(data_hora, fmt_hora)
ln()
print('',data,' '*21,f'{hora}')
ln()