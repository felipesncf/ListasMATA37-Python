n, m = map(int, input().split())
p = []

for z in range(n):
    p.append(list(map(int, input().split())))

a = int(input())
b = []
d = []
for y in range(a):
    l, c = map(int, input().split())
    b.append(l)
    b.append(c)
    d.append(b)
    b = []


for i in range(len(d)):
    if(p[d[i][0] - 1][d[i][1] - 1] == 1):
        p[d[i][0] - 1][d[i][1] - 1] = 3

retorno = False
for i in range(n):
    if(3 in p[i] and not 1 in p[i]):
        retorno = True
    else:
        retorno = False

if(retorno):
    print('HASTA LA VISTA BABY')
else:
    print('ILL BE BACK')
