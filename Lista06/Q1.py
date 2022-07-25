def sort(lista):
    n = len(lista)
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


n = int(input())
t = list(map(int, input().split()))
t = sort(t)

for i in range(8):
    print(str(t[i]), end=' ')
