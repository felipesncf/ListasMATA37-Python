p = int(input())
quantHomens = 0
quantMulheres = 0
sexo = 0
for i in range(p):
    sexo = int(input())
    if(sexo == 1):
        quantHomens += 1
    elif(sexo == 2):
        quantMulheres += 1
print(quantHomens)
print(quantMulheres)
