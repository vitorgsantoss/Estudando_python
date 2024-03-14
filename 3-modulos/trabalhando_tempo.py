from datetime import *
def delta(dias=0,horas=0,minutos=0,segundos=0):
    """Função para descobrir o tempo equivalente em dias, horas, minutos e segundos"""
    delt = timedelta(days=dias, hours= horas, minutes= minutos, seconds=segundos)
    return delt
print(delta(54,988,456,9852))