from datetime import datetime

from datetime import timedelta
from dateutil.relativedelta import relativedelta

fmt = '%Y/%m/%d %H:%M:%S'
data1= datetime.strptime('2021/05/15 22:05:30', fmt)
data2 = datetime.now().replace(microsecond=0)
# delta = timedelta(10,5)
# print(data1)
# print(data1 + delta)
delta = relativedelta(data1,data2)
print(delta)