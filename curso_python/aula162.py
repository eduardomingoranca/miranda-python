# Criando datas com modulo datetime
# datetime(ano, mes, dia)
# datetime(ano, mes, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

data_str_data = '2024/03/01 01:07:00'
data_str_data = '01/03/2024'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)