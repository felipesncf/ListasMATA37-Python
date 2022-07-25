n, m = map(int, input().split())
a = []
b = []
c = []
d = []

for z in range(n):
    a.append(list(map(int, input().split())))

for z in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        c.append(int(a[i][j] - b[i][j]))
    d.append(c)
    c = []

for i in range(n):
    for j in range(m):
        print(str(d[i][j]), end=' ')
    print()
