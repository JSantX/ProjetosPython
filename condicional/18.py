v1=int(input('Digite o primeiro valor: '))
v2=int(input('Digite o segundo valor: '))
D= v1-v2
if (D<0):
    D= v2-v1 
print(f'A diferença é {D}')