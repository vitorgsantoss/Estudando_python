from datetime import datetime
from dateutil.relativedelta import relativedelta


fmt= '%d/%m/%Y'
data= datetime(2022, 12, 20)
data_final = data + relativedelta(years=5)
diferenca = relativedelta(data_final, data)
qtd_parcelas = diferenca.years * 12 + diferenca.months
valor_parcela = 1000000/qtd_parcelas

data_parcela = data

while True:
    print(f'{datetime.strftime(data_parcela, fmt)}, {valor_parcela:.2f}')
    if data_parcela == data_final:
        break
    data_parcela += relativedelta(months=1)

print(qtd_parcelas)