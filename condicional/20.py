import math

a=float(input('Valor a: '))
b=float(input('Valor b: '))
c=float(input('Valor c: '))

delta=(b*b) - (4*a*c)

if delta<0:
    print('Não tem raiz')
else:
    x1= (-b+math.sqrt(delta))/(2*a)
    x2= (-b-math.sqrt(delta))/(2*a)
    print(f'Raízes: {x1}, {x2}')