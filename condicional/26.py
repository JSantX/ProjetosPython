v1=int(input('Valor 1: '))
v2=int(input('Valor 2: '))
maior = v1
menor = v2
if v2>v1:
    maior=v2
    menor=v1
if maior % menor ==0:
    print('É múltiplo')
else:
    print('Não é múltiplo')