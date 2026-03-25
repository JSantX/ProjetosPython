tipo = int(input('1 ou 2: '))
valor = float(input('Deposite o valor: '))

if tipo == 1:
    print(valor * 1.03)
elif tipo == 2:
    print(valor * 1.05)
else:
    print('Aplicação negada')