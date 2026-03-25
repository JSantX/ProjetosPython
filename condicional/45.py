#nao sei, to ficando louco

soma = 0
div = 0

for i in range(1, 16):
    termo = i / (i*i)
    if i % 2 == 0:
        soma -= termo
    else:
        soma += termo
for n in range(1, 225):
    if n % 2 == 0:
        div #parou aqui
print(soma)