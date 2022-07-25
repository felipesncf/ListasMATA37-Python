x = []
for z in range(10):
    x.append(list(input().split()))
for i in range(10):
    for j in range(10):
        if(x[i][j] == 't'):
            if(j < 9 and x[i][j+1] == '*'):
                x[i][j] = 'p'
            if(j > 0 and x[i][j-1] == '*'):
                x[i][j] = 'p'
            if(i < 9 and x[i+1][j] == '*'):
                x[i][j] = 'p'
            if(i > 0 and x[i-1][j] == '*'):
                x[i][j] = 'p'
        print(x[i][j], end=' ')
    print()
