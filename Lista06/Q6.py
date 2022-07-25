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


def sort(lista):
    n = len(lista)
    for fim in range(n - 1, 0, -1):
        for i in range(0, fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


def comp(item):
    return -item[0], item[1]


n, q = map(int, input().split())
x = []

for i in range(q):
    x.append(list(map(int, input().split())))

listaOrdenada = sorted(x, key=comp)
notasSelecionadas = []
idsSelecionados = []
for i in range(n):
    notasSelecionadas.append(listaOrdenada[i][0])
    idsSelecionados.append(listaOrdenada[i][1])

idsSelecionados = sort(idsSelecionados)

c = int(input())
result = ''
for _ in range(c):
    a, b = map(int, input().split())
    if(bb(idsSelecionados, b) != -1):
        result += 'Sim,'
    else:
        result += 'Nao,'

resultado = result.split(',')
resultado.pop()

for i in range(c):
    print(resultado[i])
