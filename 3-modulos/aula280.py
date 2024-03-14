from calendar import month
import locale

print(month(2023, 12))
locale.setlocale(locale.LC_ALL, '')
print(month(2023, 12))