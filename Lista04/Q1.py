n = int(input())
v = list(map(int, input().split()))
c = int(input())
encontrou = False
for i in range(n):
    if(v[i] == c):
        encontrou = True
        print(c)
        break
if(not encontrou):
    print(-1)
    