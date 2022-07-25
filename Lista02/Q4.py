x = int(input())
i = 0
quantCV = 0
quantVV = 0
quantLM = 0
while(i <= x):
    if(i == x):
        break
    quantCV += 1
    i += 1
    if(i == x):
        break
    quantVV += 1
    i += 1
    if(i == x):
        break
    quantLM += 1
    i += 1

print('Chapeuzinho Vermelho '+str(quantCV))
print('Vovozinha '+str(quantVV))
print('Lobo Mau '+str(quantLM))
