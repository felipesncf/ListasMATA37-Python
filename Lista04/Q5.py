n = int(input())
e = list(map(int, input().split()))
e = sorted(set(list(filter(lambda a: a <= 7, e))))
estrelas = ''

for i in range(len(e)):
    estrelas += str(e[i]) + ' '

print(estrelas.rstrip())
print('Saia Shenlong e realize o meu desejo') if len(
    e) == 7 else print('Nao encontramos todas')
