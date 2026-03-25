preco = float(input('Preço: '))
venda = float(input('Vendas: '))

if venda < 500 and preco < 30:
    novo = preco * 1.10
elif venda >= (500 and venda < 1000) or preco >= 30 and preco < 80:
    novo = preco * 1.15
elif venda >= 1000 and preco >= 80:
    novo = preco * 0.95
else:
    novo = preco
print (novo)