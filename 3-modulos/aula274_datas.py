from datetime import datetime


data = '17/01/2024 19:19'
formato='%d/%m/%Y %H:%M'
data_formatada = datetime.strptime(data,formato)

print(data_formatada)