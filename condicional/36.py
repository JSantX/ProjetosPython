#não sei

n = int(input())
soma = 1
fat = 1

for i in range(1, n+1):
    fat *= i
    soma += 1/fat

print(soma)