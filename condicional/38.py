maior = 999999999
menor = 0

for i in range(100):
    n = float(input())
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(maior, menor)