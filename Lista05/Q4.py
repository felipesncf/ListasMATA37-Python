n, m = map(int, input().split())
x = []
for z in range(n):
    x.append(list(map(int, input().split())))

total = 0
ovos = []
w = -1

for i in range(n):
    if(w == m-1):
        while(w >= 0):
            total += x[i][w]
            if(total < 0):
                total = 0
            w -= 1
    else:
        while(w < m-1):
            w += 1
            total += x[i][w]
            if(total < 0):
                total = 0

print(int(total))

# linhas, colunas = map(int, input().split())
# qtdOvos = 0
# matrizA = [[0] * colunas for l in range(linhas)]

# for l in range(linhas):
#     entradas = input().split()
#     matrizA[l] = list(map(int, entradas))


# n, m = map(int, input().split())
# total = 0
# x = []
# for z in range(n):
#     x.append(list(map(int, input().split())))

# for l in range(n):
#     if l % 2 == 0:
#         for c in range(0, m, 1):
#             print(str(l) + ', ' + str(c))
#             total += x[l][c]
#             if total < 0:
#                 total = 0
#     else:
#         for c in range(m-1, -1, -1):
#             print(str(l) + ', ' + str(c))
#             total += x[l][c]
#             if total < 0:
#                 total = 0
# print(total)
