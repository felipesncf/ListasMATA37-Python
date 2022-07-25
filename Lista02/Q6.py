from re import X


a, d, p = map(int, input().split(' '))
total = a + d + p
porcentagem = int((100 * total)/110)
if(porcentagem >= 0 and porcentagem <= 50):
    print('Seu pokemon nao fara progresso em batalhas')
elif(porcentagem > 50 and porcentagem <= 66):
    print('Seu pokemon esta acima da media')
elif(porcentagem > 66 and porcentagem <= 79):
    print('Seu pokemon certamente me chamou atencao')
elif(porcentagem > 79 and porcentagem <= 100):
    print('Seu pokemon e uma maravilha')
elif(porcentagem > 100):
    print('Hum, parece que houve um erro')
