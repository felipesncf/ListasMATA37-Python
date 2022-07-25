n = int(input())
x = list(map(int, input().split()))
assassinatos = ''
x.sort()
for i in range(len(x)):
    assassinatos += str(x[i]) + ' '
print(assassinatos.rstrip())
