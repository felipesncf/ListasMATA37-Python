n = int(input())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
d = list(map(int, input().split()))

w = list()
isValid = True
for i in range(n):
    w.append(u[i]+v[i])
for j in range(n):
    if(w[j] != d[j]):
        isValid = False
print('OK') if isValid == True else print('NOPE :(')
