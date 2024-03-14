import calendar
# print(calendar.calendar(1996))
# print(calendar.month(2024,11))

primeiro_dia_semana2022, ultimo_dia_fev2022 = calendar.monthrange(2022,2)
print('O primeiro dia da semana de fevereiro de 2022 foi', calendar.day_name[primeiro_dia_semana2022])
print('O último dia do mês de fevereiro de 2022 foi', ultimo_dia_fev2022)
print('O último dia da semana de fevereiro de 2022 foi',calendar.day_name[calendar.weekday(2022,12,ultimo_dia_fev2022)])