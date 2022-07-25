def sort(lista, reverse):
    n = len(lista)
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    if(reverse):
        lista.reverse()
    return lista


q, c, oc = map(str, input().split())
a = int(q)

x = []
y = []
position = 0 if c == 'N' else 1
position2 = 1 if position == 0 else 0
for i in range(a):
    x.append(input().split())
    x[i][1] = int(x[i][1])
    y.append(x[i][position])

reverse = True if oc == 'D' else False

y = sort(y, reverse)

z = []
for i in range(a):
    for j in range(a):
        if(x[j][position] == y[i]):
            z.append(x[j][position2])

nome = []
classific = []
if(position == 0):
    nome = y
    classific = z
else:
    nome = z
    classific = y

for i in range(a):
    print(nome[i] + ' ' + str(classific[i]))
