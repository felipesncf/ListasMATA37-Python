from dis import dis


def bb(lista, elem):
    esq = 0
    dir = len(lista) - 1
    isGeral = False
    while esq < dir:
        meio = esq + (dir - esq) // 2
        if elem > lista[meio]:
            esq = meio + 1
        else:
            dir = meio
    if lista[esq] == elem:
        return esq
    else:
        return -1


n = int(input())
cods = list(input().split())
x = int(input())
cods2 = list(input().split())
y = []
for _ in range(n):
    y.append(list(map(int, input().split())))

dist = 0
indices = []
for i in range(x):
    indices.append(bb(cods, cods2[i]))

lenList = len(indices)
if(lenList) >= 1:
    dist = y[0][indices[0]]
for i in range(lenList):
    if(len(indices) > 1):
        dist += y[indices[0]][indices[1]]
        indices.pop(0)
    else:
        break

print(dist)
