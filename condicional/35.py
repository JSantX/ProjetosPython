a = int(input())
b = int(input())

inicio = min(a, b)
fim = max(a, b) 

soma = 0

for i in range(inicio, fim+1):    
    if i % 2 != 0:
        soma += i

print(soma)

 #(fim+1):se eu colocasse 5, ele só iria até 4, então coloca +1 para incluir o "limite"
 #o símbolo de % é o resto de uma divisão. Ex: 4%2 !=0 (se o restante dessa divisão for diferente de 0 então ele vai fazer algum comando)
 #operações que incluem simbolos com um = no final (+=, -=, *=, /=) vão pegar uma variavel de valor JA DEFINIDO e fazer alguma coisa com ela e outro valor (+= valor da própria variavel + outro numero)
 #min e max servem para achar um valor minimo e maximo de uma lista de numeros ou um nome em ordem alfabetica