def bb(lista, elem):
    esq = 0
    dir = len(lista) - 1
    while esq <= dir:
        meio = esq+(dir - esq) // 2
        if lista[meio] == elem:
            return meio
        elif elem < lista[meio]:
            dir = meio - 1
        elif elem > meio:
            esq = meio + 1
    return -1


n = int(input())
w = list(map(int, input().split()))
p = list(map(int, input().split()))

for inicio in range(1, len(w)):
    i = inicio
    while i >= 1 and w[i] < w[i-1]:
        w[i], w[i-1] = w[i-1], w[i]
        i -= 1

for i in range(len(p)):
    if(p[i] == 0):
        break
    else:
        result = bb(w, p[i])
        if(result == -1):
            print('Nao foi visitado ainda.')
        else:
            print(result)
