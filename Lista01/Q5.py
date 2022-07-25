n = int(input())
horas = n // 3600
n -= horas * 3600
minutos = n // 60
segundos = n - (minutos * 60)
print(str(horas)+'h ' + str(minutos)+'m ' + str(segundos)+'s')
