s, n = map(int, input().split())
p = list()
result = list()
valores = ''
for i in range(s):
    p.append(int(input()))

result.append(1)

for i in range(1, n):
    for j in range(s):
        if(i % p[j] == 0):
            result.append(1)
            break
    if(len(result) != i+1):
        result.append(0)

for i in range(len(result)):
    valores += str(result[i]) + ' '
print(valores.rstrip())
