t = int(input())
p = int(input())
result = 'O Havai pode dormir tranquilo'
while(p != 0):
    if(p > t):
        result = 'ALARME'
    p = int(input())
print(result)
