n = int(input())
v = list(map(int, input().split()))

par = list()
impar = list()

parResult = ''
imparResult = ''

for i in range(n):
    if(v[i] % 2 == 0):
        par.append(v[i])
    else:
        impar.append(v[i])

for i in range(len(par)):
    parResult += str(par[i]) + ' '

for i in range(len(impar)):
    imparResult += str(impar[i]) + ' '

print(parResult.rstrip())
print(imparResult.rstrip())
