n, m = map(int, input().split())
x = []
y = []
total = 0
for z in range(n):
    x.append(list(map(int, input().split())))

for z in range(m):
    a, b = map(int, input().split())
    if(x[a][b] == 0):
        w = a
        while(w >= 0):
            if(x[w][b] == 1):
                total += 1
                x[w][b] = 2
                break
            w -= 1
print(total)
