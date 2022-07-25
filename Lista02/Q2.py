l1, p1 = map(int, input().split(' '))
l2, p2 = map(int, input().split(' '))
l3, p3 = map(int, input().split(' '))

totalL = l1 + l2 + l3
totalP = p1 + p2 + p3

if(totalL > totalP):
    print('Lucas')
elif(totalP > totalL):
    print('Pedro')
else:
    print('Empate')
