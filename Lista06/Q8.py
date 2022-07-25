def bb(lista, elem):
    elem += 1
    esq = 0
    dir = len(lista) - 1
    while esq < dir:
        meio = esq + (dir - esq) // 2
        if elem > lista[meio]:
            esq = meio + 1
        else:
            dir = meio
    return esq


def sort(lista):
    n = len(lista)
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


n, m = map(int, input().split())

y = []
x = []
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        y.append(x[j])

y = sort(y)
q = int(input())
h = list(map(int, input().split()))
for i in range(q):
    if(h[i] >= y[len(y)-1]):
        print(len(y))
    else:
        print(bb(y, h[i]))
