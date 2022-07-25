def sort(lista):
    n = len(lista)
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    lista.reverse()
    return lista


n = int(input())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))

comparador = x[0][1]
y = []
for i in range(n):
    y.append(x[i][1])

y = sort(y)

z = []
for i in range(n):
    for j in range(n):
        if(x[j][1] == y[i]):
            z.append(x[j][0])

for i in range(n):
    print(str(z[i]) + ' ' + str(y[i]))
