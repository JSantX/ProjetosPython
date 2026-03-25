n = int(input())

if n < 0:
    print("Não existe fatorial de número negativo")
else:
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    print(fat)