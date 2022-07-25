a, b = map(int, input().split(' '))
quant = 0
mult = 0
for i in range(a, b+1):
    for j in range(2, i):
        if(i % j == 0):
            mult += 1
    if(mult == 0):
        quant += 1
    mult = 0
print(quant)
