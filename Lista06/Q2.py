def sort(lista, reverse):
    n = len(lista)
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    if(reverse):
        lista.reverse()
    return lista


p = int(input())
ih = list(map(int, input().split()))
im = list(map(int, input().split()))

ih = sort(ih, True)
im = sort(im, False)

for i in range(p):
    print(str(ih[i]) + ' ' + str(im[i]))
