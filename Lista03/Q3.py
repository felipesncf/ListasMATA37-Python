paciente = input().upper()
saida = ''
while(paciente != '# 0'):
    saturacao = 'Internar' if int(paciente.split(' ')[1]) < 90 else 'Alta'
    saida += paciente[0]+' '+saturacao + '\n'
    paciente = input().upper()

print(saida)
