num = int(input('digite um numero: '))
for i in range (1,6):
    soma = num + i
    sub = num - i
    mult = num * i
    div = num / i
    print (f'soma {num} + {i} = {soma} subtração {num} - {i} = {sub} multiplicação {num} * {i} = {mult} divisão {num} / {i} = {div:.2f}')
