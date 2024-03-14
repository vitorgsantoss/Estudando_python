from pytz import timezone
from datetime import datetime

hora = datetime.now(timezone('Asia/Tokyo'))

# data = datetime.timestamp(hora)
data = datetime.fromtimestamp(2)
print(data)