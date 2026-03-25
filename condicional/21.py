n1=int(input('Nota do 1ºbimestre: '))
n2=int(input('Nota do 2ºbimestre: '))
n3=int(input('Nota do 3ºbimestre: '))
n4=int(input('Nota do 4ºbimestre: '))
M= (n1+n2+n3+n4)/4
print(M)
if (M>=6):
    print('Aluno aprovado')
elif (M>=3 and M<=6):
    print('Fazer exame')
else:
    print('Aluno retido')