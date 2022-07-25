p = int(input())
x = []
for z in range(10):
    x.append(list(map(int, input().split())))

hasPF = 'nao'
for i in range(len(x)):
    for j in range(len(x)):
        if(int(x[i][j]) == p):
            hasPF = 'sim'
            break

print(hasPF)
