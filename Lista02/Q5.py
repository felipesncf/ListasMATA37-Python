z, g = map(str, input().split())
d, c = map(str, input().split())

if(z != d):
    print('Bloqueado')
elif(z == d):
    print('Driblado')
    if(g != c):
        print('...e o goleiro pega')
    elif(g == c):
        print('Gol')
