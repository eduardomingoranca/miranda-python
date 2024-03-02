# Usando calendar para calendarios e datas
# https://docs.python.org/3/library/calendar.html
# calendar eh usado para coisas genericas de calendarios e datas.
# Com calendar, voce pode saber coisas como:
# - Qual o ultimo dia do mes (ex.: monthrange)
# - Qual o nome e numero do dia de determinada data (ex.: weekday)
# - Criar um calendario em si (ex.: monthcalendar)
# - Trabalhar com coisas especificas de calendarios (ex.: calendar, month)
# Por padrao dia da semana comeca em 0 ateh 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)